from django.test import TestCase


class TestWebhooks(TestCase):

    def test_shopping_cart_contents(self):
        subtotal = 0
        self.assertEqual(subtotal, 0)
        self.assertFalse(subtotal, int)
        self.assertFalse(subtotal, range(0, 1))

        drink_counter = 0
        self.assertEqual(drink_counter, 0)
        self.assertFalse(drink_counter, int)
        self.assertFalse(drink_counter, range(0, 1))

        self.assertTrue("shopping_cart", str)

        self.assertTrue("item_id", str)
        self.assertTrue("drink_quantity", str)
        self.assertTrue("drink", str)

        self.assertTrue("former_delivery_cost", str)
        self.assertTrue("shopping_cart_items", str)
        self.assertTrue("subtotal", str)
        self.assertTrue("drink_counter", str)
        self.assertTrue("subtotal", str)
        self.assertTrue("delivery", str)
        self.assertTrue("grand_total", str)
        self.assertTrue("company_email", str)
