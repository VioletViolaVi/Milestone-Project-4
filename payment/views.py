from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings

from .forms import DrinkOrderForm
from .models import DrinkOrder, DrinkOrderLineItem
from home.models import Drink
from shopping_cart.contexts import shopping_cart_contents

import stripe


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
            drink_order = drink_order_form.save()
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
                                    args=[drink_order.order_number]))
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


def payment_success(request, order_number):
    saved_info = request.session.get("saveInfo")
    drink_order = get_object_or_404(DrinkOrder, order_number=order_number)
    messages.success(request, f"Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {drink_order.email}.")

    if "shopping_cart" in request.session:
        del request.session["shopping_cart"]

    template = "payment/payment_success_and_history.html"
    context = {
        "drink_order": drink_order,
    }

    return render(request, template, context)
