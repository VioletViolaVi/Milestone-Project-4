from django.test import TestCase


class TestAdmin(TestCase):

    def test_drink_type_admin(self):
        list_display = ("programmatic_name", "friendly_name")
        self.assertIs(list_display, ("programmatic_name", "friendly_name"))

    def test_drink_admin(self):
        list_display = ("drink_name", "millilitres",
                        "price", "drink_type", "image")
        self.assertIs(list_display, ("drink_name", "millilitres",
                                     "price", "drink_type", "image"))
