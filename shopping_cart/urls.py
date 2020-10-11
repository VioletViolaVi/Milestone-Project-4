from django.urls import path
from . import views

urlpatterns = [
    path('', views.shopping_cart, name="shopping_cart"),
]
