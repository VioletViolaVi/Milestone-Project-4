from django.test import TestCase


class TestForms(TestCase):

    def test_user_profiles_form(self):
        self.assertTrue("user", str)

        placeholders = {
            "default_full_name": "Full Name",
            "default_phone_number": "Phone Number",
            "default_street_address1": "Street Address 1",
            "default_street_address2": "Street Address 2",
            "default_postcode": "Postal Code",
        }
        self.assertTrue(placeholders, dict)

        self.assertTrue("default_full_name", str)
        self.assertTrue("Full Name", str)
        self.assertTrue("default_phone_number", str)
        self.assertTrue("Phone Number", str)
        self.assertTrue("default_street_address1", str)
        self.assertTrue("Street Address 1", str)
        self.assertTrue("default_street_address2", str)
        self.assertTrue("Street Address ", str)
        self.assertTrue("default_postcode", str)
        self.assertTrue("Postal Code", str)

        self.assertTrue("autofocus", str)
        self.assertTrue("default_country", str)
        self.assertTrue("placeholder", str)
        self.assertTrue("class", str)
        self.assertTrue("profile-countries", str)
