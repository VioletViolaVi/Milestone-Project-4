from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Drink
from .forms import DrinkForm


def home(request):

    new_drinks = Drink.objects.filter(drink_type=1)
    juices = Drink.objects.filter(drink_type=2)
    milkshakes = Drink.objects.filter(drink_type=3)

    searched_drinks = Drink.objects.exclude(drink_type=1)
    drink_search = None
    drink_search_results = ""

    sort = None
    direction = None

    if request.GET:

        if "sort" in request.GET:
            sort_key = request.GET["sort"]
            sort = sort_key
            sort_key == "price"

            if sort_key == "drink_name":
                sort_key == "lower_case_name"
                new_drinks = new_drinks.annotate(
                    lower_case_name=Lower("drink_name"))
                juices = juices.annotate(lower_case_name=Lower("drink_name"))
                milkshakes = milkshakes.annotate(
                    lower_case_name=Lower("drink_name"))
                searched_drinks = searched_drinks.annotate(
                    lower_case_name=Lower("drink_name"))

            if "direction" in request.GET:
                direction = request.GET["direction"]
                if direction == "desc":
                    sort_key = f"-{sort_key}"
            new_drinks = new_drinks.order_by(sort_key)
            juices = juices.order_by(sort_key)
            milkshakes = milkshakes.order_by(sort_key)
            searched_drinks = searched_drinks.order_by(sort_key)

        if "search" in request.GET:
            drink_search = request.GET["search"]
            drink_search_results = searched_drinks.filter(
                Q(drink_name__icontains=drink_search))

    drink_sorting = f"{sort}_{direction}"

    context = {
        "new_drinks": new_drinks,
        "juices": juices,
        "milkshakes": milkshakes,
        "drink_search_results": drink_search_results,
        "typed_in_search": drink_search,
        "drink_sorting": drink_sorting,
        "this_is_the_homepage":  True,
    }

    # shows homepage
    return render(request, "home/index.html", context)


def add_drink(request):
    # adds drinks to shop
    if request.method == "POST":
        form = DrinkForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Drink successfully added!")
            print("issue here")
            print(messages.success(request, "Drink successfully added!"))
            return redirect(reverse("add_drink"))
        else:
            messages.error(request,
                           "Failed to add drink. Please \
                                ensure the form is valid.")
    else:
        form = DrinkForm()

    template = "home/add_drink.html"
    context = {
        "form": form,
    }

    return render(request, template, context)
