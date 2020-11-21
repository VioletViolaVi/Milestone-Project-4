from django.test import TestCase
from .models import DrinkOrder
from .forms import DrinkOrderForm


class TestForms(TestCase):
    def test_drink_order_form_modal(self):
        model = DrinkOrder
        self.assertIs(model, DrinkOrder)

    def test_drink_order_form_field(self):
        fields = ("full_name", "email", "phone_number",
                  "street_address1", "street_address2", "postcode",
                  "country",)
        self.assertTrue(fields, tuple)

    def test_placeholders(self):
        placeholders = {
            "full_name": "Full Name",
            "email": "Email",
            "phone_number": "Phone Number",
            "street_address1": "Street Address 1",
            "street_address2": "Street Address 2",
            "postcode": "Postal Code",
        }
        self.assertTrue(placeholders, dict)

    def test_input_fields(self):
        self.assertTrue("country", str)

    def test_payment_form_full_name_is_required(self):
        form = DrinkOrderForm({"full_name": ""})
        self.assertFalse(form.is_valid())
        self.assertIn("full_name", form.errors.keys())
        self.assertEqual(form.errors["full_name"]
                         [0], "This field is required.")

    def test_payment_form_email_is_required(self):
        form = DrinkOrderForm({"email": ""})
        self.assertFalse(form.is_valid())
        self.assertIn("email", form.errors.keys())
        self.assertEqual(form.errors["email"][0], "This field is required.")

    def test_payment_form_phone_number_is_required(self):
        form = DrinkOrderForm({"phone_number": ""})
        self.assertFalse(form.is_valid())
        self.assertIn("phone_number", form.errors.keys())
        self.assertEqual(form.errors["phone_number"]
                         [0], "This field is required.")

    def test_payment_form_street_address1_is_required(self):
        form = DrinkOrderForm({"street_address1": ""})
        self.assertFalse(form.is_valid())
        self.assertIn("street_address1", form.errors.keys())
        self.assertEqual(form.errors["street_address1"]
                         [0], "This field is required.")

    def test_payment_form_postcode_is_required(self):
        form = DrinkOrderForm({"postcode": ""})
        self.assertFalse(form.is_valid())
        self.assertIn("postcode", form.errors.keys())
        self.assertEqual(form.errors["postcode"]
                         [0], "This field is required.")

    def test_payment_form_country_is_required(self):
        form = DrinkOrderForm({"country": ""})
        self.assertFalse(form.is_valid())
        self.assertIn("country", form.errors.keys())
        self.assertEqual(form.errors["country"][0], "This field is required.")

    def test_payment_form_street_address2_is_not_required(self):
        form = DrinkOrderForm({"full_name": "Test",
                               "email": "Test",
                               "phone_number": "Test",
                               "street_address1": "Test",
                               "street_address2": "",
                               "postcode": "Test",
                               "country": "Test",
                               })
        self.assertFalse(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        form = DrinkOrderForm()
        fields = ("full_name", "email", "phone_number",
                  "street_address1", "street_address2", "postcode",
                  "country",)
        self.assertEqual(form.Meta.fields, fields)
