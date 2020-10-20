from django.urls import path
from . import views

urlpatterns = [
    path("", views.payment1, name="payment1"),
    path("payment_history/<order_number>",
         views.payment_success1, name="payment_success1"),
]
