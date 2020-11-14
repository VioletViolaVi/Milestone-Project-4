from django.test import TestCase


class TestApps(TestCase):

    def test_shopping_cart_config(self):
        name = "shopping_cart"
        self.assertIs(name, "shopping_cart")
        self.assertTrue(name, str)
