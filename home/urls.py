from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("add/", views.add_drink, name="add_drink"),
    path("edit/", views.edit_drink, name="edit_drink"),
    path("delete/", views.delete_drink, name="delete_drink"),
]
