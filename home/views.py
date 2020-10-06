from django.shortcuts import render
from .models import Drink


def home(request):

    new_drinks = Drink.objects.filter(drink_type=1)
    juices = Drink.objects.filter(drink_type=2)
    milkshakes = Drink.objects.filter(drink_type=3)

    context = {
        "new_drinks": new_drinks,
        "juices": juices,
        "milkshakes": milkshakes,
    }

    # shows homepage
    return render(request, "home/index.html", context)
