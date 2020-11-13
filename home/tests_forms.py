from django.test import TestCase
from .models import Drink, Drink_type
from django import forms
from .widgets import CustomClearableFileInput


class TestForms(TestCase):
    def test_drink_form_modal(self):
        model = Drink
        self.assertIs(model, Drink)

    def test_drink_form_field(self):
        fields = "__all__"
        self.assertIs(fields, "__all__")

    def test_imagex_field(self):
        image = forms.ImageField(widget=CustomClearableFileInput)
        self.assertIs(image, forms.ImageField(widget=CustomClearableFileInput))

    def test_drink_form_drink_types(self):
        drink_types = Drink_type.objects.all()
        self.assertIs(drink_types, Drink_type.objects.all())
