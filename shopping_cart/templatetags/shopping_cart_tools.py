from django import template


register = template.Library()


@register.filter(name="calc_subtotal")
def calc_subtotal(price, drink_quantity):
    return price * drink_quantity
