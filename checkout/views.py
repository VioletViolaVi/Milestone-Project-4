from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import DrinkOrderForm


def checkout(request):
    shopping_cart = request.session.get("shopping_cart", {})
    if not shopping_cart:
        messages.error(request, "There's nothing in your shopping cart.")
        return redirect(reverse('home'))

    drink_order_form = DrinkOrderForm()
    template = "checkout/checkout.html"
    context = {
        'drink_order_form': drink_order_form,
        "stripe_public_key": "pk_test_51HUF24FyWkzyv3XJCItWmCeUd8D0vZOhRger4iVLVRZQShSmBC8H35voHb2Pj1LJ7Co5YGX4bAcLEzBk64Ome0og00jDR0YrzD",
        "client_secret": "test client secret",
    }

    return render(request, template, context)
