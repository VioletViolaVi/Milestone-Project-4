from django.urls import path
from . import views

urlpatterns = [
    path("", views.user_profiles, name="user_profiles"),
    path("drink_order_history/<drink_order_number>/",
         views.drink_order_history, name="drink_order_history"),
]
