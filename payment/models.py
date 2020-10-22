import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from django_countries.fields import CountryField

from home.models import Drink
from user_profiles.models import UserProfiles


class DrinkOrder(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(
        UserProfiles, on_delete=models.SET_NULL,
        null=True, blank=False, related_name="drink_orders")
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=False)
    country = CountryField(blank_label="Country *", null=False, blank=False)
    subtotal = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    delivery_cost = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    date = models.DateTimeField(auto_now_add=True)
    original_shopping_cart = models.TextField(
        null=False, blank=False, default="")
    stripe_pid = models.CharField(
        max_length=254, null=False, blank=False, default="")

    def _generate_order_number(self):
        return uuid.uuid4().hex.upper()

    def update_total(self):
        self.subtotal = self.lineitems.aggregate(Sum("lineitem_total"))[
            "lineitem_total__sum"] or 0
        self.delivery_cost = settings.DELIVERY_COST
        self.grand_total = self.subtotal + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class DrinkOrderLineItem(models.Model):
    drink_order = models.ForeignKey(
        DrinkOrder, null=False, blank=False,
        on_delete=models.CASCADE, related_name="lineitems")
    drink = models.ForeignKey(
        Drink, null=False, blank=False, on_delete=models.CASCADE)
    drink_quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False,
        blank=False, editable=False)

    def save(self, *args, **kwargs):
        self.lineitem_total = self.drink.price * self.drink_quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Drink order number: {self.drink_order.order_number}"
