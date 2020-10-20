from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import DrinkOrderLineItem1


@receiver(post_save, sender=DrinkOrderLineItem1)
def update_on_save(sender, instance, created, **kwargs):

    instance.order.update_total()


@receiver(post_delete, sender=DrinkOrderLineItem1)
def update_on_delete(sender, instance, **kwargs):

    instance.order.update_total()
