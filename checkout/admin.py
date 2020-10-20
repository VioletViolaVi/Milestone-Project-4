from django.contrib import admin
from .models import DrinkOrder1, DrinkOrderLineItem1


class DrinkOrderLineItemAdminInline(admin.TabularInline):
    model = DrinkOrderLineItem1
    readonly_fields = ("lineitem_total",)


class DrinkOrderAdmin(admin.ModelAdmin):
    inlines = (DrinkOrderLineItemAdminInline,)

    readonly_fields = ("order_number", "date",
                       "delivery_cost", "subtotal",
                       "grand_total",)

    fields = ("order_number", "full_name", "email", "phone_number",
              "street_address1", "street_address2", "postcode",
              "country", "subtotal", "delivery_cost",
              "grand_total", "date")

    list_display = ("order_number", "date", "full_name",
                    "subtotal", "delivery_cost",
                    "grand_total",)

    ordering = ('-date',)


admin.site.register(DrinkOrder1, DrinkOrderAdmin)
