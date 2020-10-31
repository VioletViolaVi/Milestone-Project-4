from django.contrib import admin
from .models import Drink_type, Drink, About_us_section, About_us


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


class About_us_section_admin(admin.ModelAdmin):
    list_display = (
        "programmatic_name",
        "friendly_name",
    )


class About_us_admin(admin.ModelAdmin):
    list_display = (
        "title",
        "paragraph",
        "section",
        "image",
        "image_description",
    )


admin.site.register(About_us_section, About_us_section_admin)
admin.site.register(About_us, About_us_admin)
