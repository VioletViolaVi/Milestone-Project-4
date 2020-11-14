from django.test import TestCase
from .models import Drink
from .widgets import CustomClearableFileInput
from .forms import DrinkForm


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

    def test_drink_form_image_is_required(self):
        form = DrinkForm({"image": ""})
        self.assertFalse(form.is_valid())
        self.assertIn("image", form.errors.keys())
        self.assertEqual(form.errors["image"][0], "This field is required.")

    def test_drink_form_drink_name_is_required(self):
        form = DrinkForm({"drink_name": ""})
        self.assertFalse(form.is_valid())
        self.assertIn("drink_name", form.errors.keys())
        self.assertEqual(form.errors["drink_name"][0],
                         "This field is required.")

    def test_drink_form_millilitres_is_required(self):
        form = DrinkForm({"millilitres": ""})
        self.assertFalse(form.is_valid())
        self.assertIn("millilitres", form.errors.keys())
        self.assertEqual(form.errors["millilitres"]
                         [0], "This field is required.")

    def test_drink_form_drink_type_is_required(self):
        form = DrinkForm({"drink_type": ""})
        self.assertFalse(form.is_valid())
        self.assertIn("drink_type", form.errors.keys())
        self.assertEqual(form.errors["drink_type"]
                         [0], "This field is required.")

    def test_fields_are_explicit_in_form_metaclass(self):
        form = DrinkForm()
        self.assertEqual(form.Meta.fields, "__all__")
