from django.conf import settings


def shopping_cart_contents(request):

    former_delivery_cost = settings.FORMER_DELIVERY_COST

    shopping_cart_items = []

    total = 0
    drink_count = 0

    subtotal = total
    delivery = settings.DELIVERY_COST
    grand_total = delivery + total

    context = {
        "former_delivery_cost": former_delivery_cost,
        "shopping_cart_items": shopping_cart_items,
        "total": total,
        "drink_count": drink_count,
        "subtotal": subtotal,
        "delivery": settings.DELIVERY_COST,
        "grand_total": grand_total,
    }

    return context
