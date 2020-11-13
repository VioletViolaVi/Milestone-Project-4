from django.test import TestCase


class TestApps(TestCase):

    def test_payment_config(self):
        name = "payment"
        self.assertIs(name, "payment")
        self.assertTrue(name, str)
