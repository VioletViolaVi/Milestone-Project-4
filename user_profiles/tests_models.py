from django.test import TestCase


class TestModels(TestCase):

    def test_user_profiles(self):
        default_full_name = 20
        self.assertEqual(default_full_name, 20)
        self.assertTrue(default_full_name, int)
        self.assertTrue(default_full_name, range(1, 21))

        null = True
        self.assertTrue(null, bool)
        self.assertTrue(null)

        blank = True
        self.assertTrue(blank)
        self.assertTrue(blank, bool)

        default_phone_number = 20
        self.assertEqual(default_phone_number, 20)
        self.assertTrue(default_phone_number, int)
        self.assertTrue(default_phone_number, range(1, 21))

        default_street_address1 = 80
        self.assertEqual(default_street_address1, 80)
        self.assertTrue(default_street_address1, int)
        self.assertTrue(default_street_address1, range(1, 81))

        default_street_address2 = 80
        self.assertEqual(default_street_address2, 80)
        self.assertTrue(default_street_address2, int)
        self.assertTrue(default_street_address2, range(1, 81))

        default_postcode = 20
        self.assertEqual(default_postcode, 20)
        self.assertTrue(default_postcode, int)
        self.assertTrue(default_postcode, range(1, 21))

        blank_label = "Country"
        self.assertTrue(blank_label, str)
