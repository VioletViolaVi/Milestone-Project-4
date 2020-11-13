from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import DrinkOrderLineItem


@receiver(post_save, sender=DrinkOrderLineItem)
def update_on_save(sender, instance, created, **kwargs):

    instance.drink_order.update_total()


@receiver(post_delete, sender=DrinkOrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    instance.drink_order.update_total()
