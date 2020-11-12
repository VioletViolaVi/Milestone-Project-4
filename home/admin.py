from django.contrib import admin
from .models import Drink_type, Drink


class Drink_type_admin(admin.ModelAdmin):
    list_display = (
        "programmatic_name",
        "friendly_name",
    )


class Drink_admin(admin.ModelAdmin):
    list_display = (
        "drink_name",
        "millilitres",
        "price",
        "drink_type",
        "image",
    )


admin.site.register(Drink_type, Drink_type_admin)
admin.site.register(Drink, Drink_admin)
