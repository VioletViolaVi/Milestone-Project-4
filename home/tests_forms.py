from django.test import TestCase
from .models import Drink


class TestForms(TestCase):
    def test_drink_form_modal(self):
        model = Drink
        self.assertIs(model, Drink)

    def test_drink_form_field(self):
        fields = "__all__"
        self.assertIs(fields, "__all__")
