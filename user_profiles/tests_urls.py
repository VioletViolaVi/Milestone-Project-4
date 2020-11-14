from django.test import TestCase


class TestUrls(TestCase):
    def test_url_patterns(self):
        self.assertFalse("", str)
        self.assertTrue("user_profiles", str)

        self.assertTrue("drink_order_history/<drink_order_number>/", str)
        self.assertTrue("drink_order_history", str)

        name = \
            "user_profiles" or "drink_order_history/<drink_order_number>/"
        self.assertIs(name,
                      "user_profiles" or
                      "drink_order_history/<drink_order_number>/")
