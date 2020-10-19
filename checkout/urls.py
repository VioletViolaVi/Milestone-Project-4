from django.urls import path
from . import views

urlpatterns = [
    path("", views.payment, name="payment"),
    path("payment_history/<order_number>",
         views.payment_success, name="payment_success"),
]
