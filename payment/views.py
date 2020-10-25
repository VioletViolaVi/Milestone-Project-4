from django.shortcuts import (render, redirect, reverse,
                              get_object_or_404, HttpResponse)
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import DrinkOrderForm
from .models import DrinkOrder, DrinkOrderLineItem
from home.models import Drink
from user_profiles.models import UserProfiles
from user_profiles.forms import UserProfilesForm
from shopping_cart.contexts import shopping_cart_contents

import stripe
import json


@require_POST
def cache_payment_data(request):
    try:
        pid = request.POST.get("client_secret").split("_secret")[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            "shopping_cart": json.dumps(
                request.session.get("shopping_cart", {})),
            "saveInfo": request.POST.get("saveInfo"),
            "username": request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, "Sorry, your payment cannot be \
            processed right now. Please try again later.")
        return HttpResponse(content=e, status=400)


def payment(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        shopping_cart = request.session.get("shopping_cart", {})
        form_data = {
            "full_name": request.POST["full_name"],
            "email": request.POST["email"],
            "phone_number": request.POST["phone_number"],
            "street_address1": request.POST["street_address1"],
            "street_address2": request.POST["street_address2"],
            "postcode": request.POST["postcode"],
            "country": request.POST["country"],
        }
        drink_order_form = DrinkOrderForm(form_data)

        if drink_order_form.is_valid():
            drink_order = drink_order_form.save(commit=False)
            pid = request.POST.get("client_secret").split("_secret")[0]
            drink_order.stripe_pid = pid
            drink_order.original_shopping_cart = json.dumps(shopping_cart)
            drink_order.save()
            for item_id, item_data in shopping_cart.items():
                try:
                    drink = Drink.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        drink_order_line_item = DrinkOrderLineItem(
                            drink_order=drink_order,
                            drink=drink,
                            drink_quantity=item_data,
                        )
                        drink_order_line_item.save()
                except Drink.DoesNotExist:
                    messages.error(
                        request, ("One of the items in your shopping \
                             cart wasn't found in our database. \
                                 Please call us for assistance!"))

                    drink_order.delete()
                    return redirect(reverse("shopping_cart"))

            request.session["saveInfo"] = "saveInfo" in request.POST
            return redirect(reverse("payment_success",
                                    args=[drink_order.drink_order_number]))
        else:
            messages.error(
                request, "There was an error with your form. \
                    Please check your information again.")
    else:
        shopping_cart = request.session.get("shopping_cart", {})
        if not shopping_cart:
            # not showing!!!!
            messages.error(request, "There's nothing in your shopping cart.")
            return redirect(reverse('home'))

        current_shopping_cart = shopping_cart_contents(request)
        grand_total = current_shopping_cart["grand_total"]
        stripe_total = round(grand_total * 100)

        current_shopping_cart = shopping_cart_contents(request)
        total = current_shopping_cart["grand_total"]
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )
        drink_order_form = DrinkOrderForm()

    if not stripe_public_key:
        messages.warning(request, "Stripe public key is missing. \
            Did you forget to set it in your environment?")

    template = "payment/payment.html"
    context = {
        "drink_order_form": drink_order_form,
        "stripe_public_key": stripe_public_key,
        "client_secret": intent.client_secret,
    }

    return render(request, template, context)


def payment_success(request, drink_order_number):
    print("success")
    saved_info = request.session.get("saveInfo")
    drink_order = get_object_or_404(DrinkOrder,
                                    drink_order_number=drink_order_number)
    if request.user.is_authenticated:
        user_profiles = UserProfiles.objects.get(user=request.user)
        # Attach user's profile to drink order
        drink_order.user_profiles = user_profiles
        drink_order.save()

        # Save user's info
        if saved_info:
            user_profiles_data = {
                "default_phone_number": drink_order.phone_number,
                "default_street_address1": drink_order.street_address1,
                "default_street_address2": drink_order.street_address2,
                "default_postcode": drink_order.postcode,
                "default_country": drink_order.country,
            }
            user_profiles_form = UserProfilesForm(
                user_profiles_data, instance=user_profiles)
            if user_profiles_form.is_valid():
                user_profiles_form.save()

    messages.success(request, f"Order successfully processed! \
        Your order number is {drink_order_number}. A confirmation \
        email will be sent to {drink_order.email}.")

    if "shopping_cart" in request.session:
        del request.session["shopping_cart"]

    template = "payment/payment_success.html"
    context = {
        "drink_order": drink_order,
    }

    return render(request, template, context)
