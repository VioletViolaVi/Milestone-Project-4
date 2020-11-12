from django.urls import path
from . import views

urlpatterns = [
    path("", views.about_us, name="about_us"),
    path("append1/",
         views.append_about_us, name="append_about_us"),
    path("change1/<int:about_us_id>",
         views.change_about_us, name="change_about_us"),
    path("remove1/<int:about_us_id>",
         views.remove_about_us, name="remove_about_us"),
]
