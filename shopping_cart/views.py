from django.shortcuts import render, redirect


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
    print(request.session["shopping_cart"])
    return redirect(redirect_url)
