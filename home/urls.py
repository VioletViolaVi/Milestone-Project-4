from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("add/", views.add_drink, name="add_drink"),
    path("edit/<int:drink_id>", views.edit_drink, name="edit_drink"),
    path("delete/<int:drink_id>", views.delete_drink, name="delete_drink"),
    path("change/<int:about_us_id>",
         views.change_about_us, name="change_about_us"),
    path("remove/<int:about_us_id>",
         views.remove_about_us, name="remove_about_us"),
]
