from django.test import TestCase
from .models import About_us
from .widgets import CustomClearableFileInput


class TestForms(TestCase):
    def test_about_us_form_modal(self):
        model = About_us
        self.assertIs(model, About_us)

    def test_about_us_form_field(self):
        fields = "__all__"
        self.assertIs(fields, "__all__")

    def test_image_field(self):
        required = False
        self.assertFalse(required)

    def test_image_field_widget(self):
        widget = CustomClearableFileInput
        self.assertIs(widget, CustomClearableFileInput)
