from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path("", views.payment, name="payment"),
    path(
        "payment_success/<drink_order_number>",
        views.payment_success,
        name="payment_success"),
    path("cache_payment_data/", views.cache_payment_data,
         name="cache_payment_data"),
    path("wh/", webhook, name="webhook"),
]
