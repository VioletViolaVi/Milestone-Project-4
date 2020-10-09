from django.shortcuts import render
from django.db.models import Q
from .models import Drink


def home(request):

    new_drinks = Drink.objects.filter(drink_type=1)
    juices = Drink.objects.filter(drink_type=2)
    milkshakes = Drink.objects.filter(drink_type=3)

    searchable_drinks = Drink.objects.exclude(drink_type=1)
    drink_search = None
    drink_search_results = ""

    if request.GET:
        if "search" in request.GET:
            drink_search = request.GET["search"]

            drink_search_results = searchable_drinks.filter(
                Q(drink_name__icontains=drink_search))

    context = {
        "new_drinks": new_drinks,
        "juices": juices,
        "milkshakes": milkshakes,
        "drink_search_results": drink_search_results,
        "typed_in_search": drink_search,
    }

    # shows homepage
    return render(request, "home/index.html", context)
