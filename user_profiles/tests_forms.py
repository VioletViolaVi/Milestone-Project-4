from django.test import TestCase
from .forms import UserProfilesForm


class TestForms(TestCase):

    def test_user_profiles_form(self):
        self.assertTrue("user", str)

        placeholders = {
            "default_phone_number": "Phone Number",
            "default_street_address1": "Street Address 1",
            "default_street_address2": "Street Address 2",
            "default_postcode": "Postal Code",
        }
        self.assertTrue(placeholders, dict)

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

    def test_user_profiles_form_phone_number_is_not_required(self):
        form = UserProfilesForm({"phone_number": "",
                                 "street_address1": "Test",
                                 "street_address2": "Test",
                                 "postcode": "Test",
                                 "country": "Test",
                                 })
        self.assertTrue(form.is_valid())

    def test_user_profiles_form_street_address1_is_not_required(self):
        form = UserProfilesForm({"phone_number": "Test",
                                 "street_address1": "",
                                 "street_address2": "Test",
                                 "postcode": "Test",
                                 "country": "Test",
                                 })
        self.assertTrue(form.is_valid())

    def test_user_profiles_form_street_address2_is_not_required(self):
        form = UserProfilesForm({"phone_number": "Test",
                                 "street_address1": "Test",
                                 "street_address2": "",
                                 "postcode": "Test",
                                 "country": "Test",
                                 })
        self.assertTrue(form.is_valid())

    def test_user_profiles_form_postcode_is_not_required(self):
        form = UserProfilesForm({"phone_number": "Test",
                                 "street_address1": "Test",
                                 "street_address2": "Test",
                                 "country": "Test",
                                 "postcode": "",
                                 })
        self.assertTrue(form.is_valid())

    def test_user_profiles_form_country_is_not_required(self):
        form = UserProfilesForm({"phone_number": "Test",
                                 "street_address1": "Test",
                                 "street_address2": "Test",
                                 "country": "",
                                 "postcode": "Test",
                                 })
        self.assertTrue(form.is_valid())

    def test_user_is_excluded_form_metaclass(self):
        form = UserProfilesForm()
        exclude = ("user",)
        self.assertEqual(form.Meta.exclude, exclude)
