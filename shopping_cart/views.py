from django.shortcuts import render, redirect, reverse


def shopping_cart(request):

    # shows items in shopping cart
    return render(request, "shopping_cart/shopping_cart.html")


def add_to_shopping_cart(request, item_id):
    # add quantity of specified drink to cart

    drink_quantity = int(request.POST.get("drinkSelections"))
    redirect_url = request.POST.get("redirect_url")
    shopping_cart = request.session.get("shopping_cart", {})

    if item_id in list(shopping_cart.keys()):
        shopping_cart[item_id] += drink_quantity
    else:
        shopping_cart[item_id] = drink_quantity

    request.session["shopping_cart"] = shopping_cart

    return redirect(redirect_url)


def edit_shopping_cart(request, item_id):
    # edit quantity of specified drink in cart

    shopping_cart = request.session.get("shopping_cart", {})
    edited_drink_quantity = int(request.POST.get("editDrinks"))

    edited_drink_quantity.save()

    if edited_drink_quantity.save() > 0:
        shopping_cart[item_id] = edited_drink_quantity.save()
    else:
        shopping_cart.pop[item_id]

    request.session["shopping_cart"] = shopping_cart

    return redirect(reverse("shopping_cart"))
