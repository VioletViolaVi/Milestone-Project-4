from django.urls import path
from . import views

urlpatterns = [
    path('', views.shopping_cart, name="shopping_cart"),
    path('add/<int:item_id>/', views.add_to_shopping_cart,
         name="add_to_shopping_cart"),
    path('edit/<int:item_id>/', views.edit_shopping_cart,
         name="edit_shopping_cart"),
    path('delete/<int:item_id>/', views.delete_shopping_cart_item,
         name="delete_shopping_cart_item"),
]
