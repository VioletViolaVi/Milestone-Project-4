from django.urls import path
from . import views

urlpatterns = [
    path('', views.shopping_cart, name="shopping_cart"),
    path('add/<item_id>/', views.add_to_shopping_cart,
         name="add_to_shopping_cart"),
    path('edit/<item_id>/', views.edit_shopping_cart,
         name="edit_shopping_cart"),
]
