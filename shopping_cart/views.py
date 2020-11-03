from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404)
from django.contrib import messages
from home.models import Drink


def shopping_cart(request):
    # shows items in shopping cart
    return render(request, "shopping_cart/shopping_cart.html")


def add_to_shopping_cart(request, item_id):
    # adds quantity of specified drink to cart
    drink = get_object_or_404(Drink, pk=item_id)
    drink_quantity = int(request.POST.get("drinkSelections"))
    redirect_url = request.POST.get("redirect_url")
    shopping_cart = request.session.get("shopping_cart", {})

    if item_id in list(shopping_cart.keys()):
        shopping_cart[item_id] += drink_quantity
        if drink_quantity <= 1:
            messages.info(request,
                          f"{drink_quantity}x {drink.drink_name.capitalize()} \
                                  has been added to your shopping cart.")
        else:
            messages.info(request,
                          f"{drink_quantity}x {drink.drink_name.capitalize()}s \
                                  have been added to your shopping cart.")
    else:
        shopping_cart[item_id] = drink_quantity
        if drink_quantity <= 1:
            messages.info(request,
                          f"{drink_quantity}x {drink.drink_name.capitalize()} \
                                  has been added to your shopping cart.")
        else:
            messages.info(request,
                          f"{drink_quantity}x {drink.drink_name.capitalize()}s \
                                  have been added to your shopping cart.")

    request.session["shopping_cart"] = shopping_cart

    return redirect(redirect_url)


def edit_shopping_cart(request, item_id):
    # edits quantity of specified drink in cart
    drink_quantity = int(request.POST.get("editDrinks"))
    shopping_cart = request.session.get("shopping_cart", {})

    if drink_quantity > 0 and drink_quantity <= 100:
        shopping_cart[item_id] = drink_quantity
    else:
        messages.info(request, "Please pick a number from 1-100.")
        return render(request, "shopping_cart/shopping_cart.html")

    request.session["shopping_cart"] = shopping_cart

    return redirect(reverse("shopping_cart"))


def delete_shopping_cart_item(request, item_id):
    # deletes specified drink in cart
    try:
        shopping_cart = request.session.get("shopping_cart", {})
        shopping_cart.pop(item_id)
        request.session["shopping_cart"] = shopping_cart
        return redirect(reverse("shopping_cart"))
    except Exception as e:
        return HttpResponse(status=500)
