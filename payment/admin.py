from django.contrib import admin
from .models import DrinkOrder, DrinkOrderLineItem


class DrinkOrderLineItemAdminInline(admin.TabularInline):
    model = DrinkOrderLineItem
    readonly_fields = ("lineitem_total",)


class DrinkOrderAdmin(admin.ModelAdmin):
    inlines = (DrinkOrderLineItemAdminInline,)

    readonly_fields = ("drink_order_number", "date",
                       "delivery_cost", "subtotal",
                       "grand_total",
                       "original_shopping_cart",
                       "stripe_pid")

    fields = ("drink_order_number", "full_name",
              "user_profiles", "email",
              "phone_number", "street_address1",
              "street_address2", "postcode",
              "country", "subtotal",
              "delivery_cost", "grand_total",
              "date", "original_shopping_cart",
              "stripe_pid")

    list_display = ("drink_order_number", "date",
                    "full_name", "subtotal",
                    "delivery_cost", "grand_total",)

    ordering = ('-date',)


admin.site.register(DrinkOrder, DrinkOrderAdmin)
