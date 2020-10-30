from django.contrib import admin
from .models import Drink_type, Drink, About_us_section, About_us


class Drink_type_admin(admin.ModelAdmin):
    list_display = (
        "programmatic_name",
        "friendly_name",
    )


class Drink_admin(admin.ModelAdmin):
    list_display = (
        "image",
        "drink_name",
        "price",
        "millilitres",
        "drink_type",
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
        "image",
        "image_description",
        "title",
        "paragraph",
        "section",
    )


admin.site.register(About_us_section, About_us_section_admin)
admin.site.register(About_us, About_us_admin)
