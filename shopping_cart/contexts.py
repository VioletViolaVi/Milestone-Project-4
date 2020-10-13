from django.conf import settings
from django.shortcuts import get_object_or_404
from home.models import Drink


def shopping_cart_contents(request):

    former_delivery_cost = settings.FORMER_DELIVERY_COST

    shopping_cart_items = []
    subtotal = 0
    drink_counter = 0
    shopping_cart = request.session.get("shopping_cart", {})

    delivery = settings.DELIVERY_COST
    grand_total = delivery + subtotal

    for item_id, drink_quantity in shopping_cart.items():
        drink = get_object_or_404(Drink, pk=item_id)
        subtotal += drink_quantity * drink.price
        drink_counter += drink_quantity
        shopping_cart_items.append({
            "item_id": item_id,
            "drink_quantity": drink_quantity,
            "drink": drink,
        })

    context = {
        "former_delivery_cost": former_delivery_cost,
        "shopping_cart_items": shopping_cart_items,
        "subtotal": subtotal,
        "drink_counter": drink_counter,
        "subtotal": subtotal,
        "delivery": settings.DELIVERY_COST,
        "grand_total": grand_total,
    }

    return context
