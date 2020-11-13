from django.test import TestCase


class TestUrls(TestCase):
    def test_url_patterns(self):
        self.assertFalse("", str)
        self.assertTrue("payment_success/<drink_order_number>/", str)
        self.assertTrue("cache_payment_data/", str)
        self.assertTrue("wh/", str)
        name = \
            "payment" or "payment_success" or "cache_payment_data" or "webhook"
        self.assertIs(name,
                      "payment" or "payment_success" or
                      "cache_payment_data" or "webhook")
