from django.shortcuts import render


def shopping_cart(request):

    # shows items in shopping cart
    return render(request, "shopping_cart/shopping_cart.html")
