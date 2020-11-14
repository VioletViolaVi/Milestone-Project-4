from django.test import TestCase
from .models import About_us
from .widgets import CustomClearableFileInput
from .forms import AboutUsForm


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

    def test_about_us_form_image_and_image_description_are_not_required(self):
        form = AboutUsForm({"title": "Test",
                            "paragraph": "Test",
                            "section": "Test",
                            })
        self.assertFalse(form.is_valid())

    def test_about_us_form_title_is_required(self):
        form = AboutUsForm({"title": ""})
        self.assertFalse(form.is_valid())
        self.assertIn("title", form.errors.keys())
        self.assertEqual(form.errors["title"][0], "This field is required.")

    def test_about_us_form_paragraph_is_required(self):
        form = AboutUsForm({"paragraph": ""})
        self.assertFalse(form.is_valid())
        self.assertIn("paragraph", form.errors.keys())
        self.assertEqual(form.errors["paragraph"][0],
                         "This field is required.")

    def test_about_us_form_section_is_required(self):
        form = AboutUsForm({"section": ""})
        self.assertFalse(form.is_valid())
        self.assertIn("section", form.errors.keys())
        self.assertEqual(form.errors["section"][0], "This field is required.")

    def test_fields_are_explicit_in_form_metaclass(self):
        form = AboutUsForm()
        self.assertEqual(form.Meta.fields, "__all__")
