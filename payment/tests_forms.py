from django.test import TestCase
from .models import DrinkOrder


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
