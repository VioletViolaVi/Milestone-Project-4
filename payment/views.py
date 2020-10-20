from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import DrinkOrderForm


def payment(request):
    shopping_cart = request.session.get("shopping_cart", {})
    if not shopping_cart:
        # not showing!!!!
        messages.error(request, "There's nothing in your shopping cart.")
        return redirect(reverse('home'))

    drink_order_form = DrinkOrderForm()
    template = "payment/payment.html"
    context = {
        "drink_order_form": drink_order_form,
    }

    return render(request, template, context)
