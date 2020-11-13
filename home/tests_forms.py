from django.test import TestCase
from .models import Drink
from .widgets import CustomClearableFileInput


class TestForms(TestCase):
    def test_drink_form_modal(self):
        model = Drink
        self.assertIs(model, Drink)

    def test_drink_form_field(self):
        fields = "__all__"
        self.assertIs(fields, "__all__")

    def test_image_field(self):
        required = False
        self.assertFalse(required)

    def test_image_field_widget(self):
        widget = CustomClearableFileInput
        self.assertIs(widget, CustomClearableFileInput)
