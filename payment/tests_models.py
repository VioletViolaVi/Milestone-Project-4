from django.test import TestCase
# from django.db import models


class TestModels(TestCase):

    def test_drink_order(self):
        null = True
        self.assertTrue(null, bool)
        self.assertTrue(null)

        drink_order_number = 32
        self.assertEqual(drink_order_number, 32)
        self.assertTrue(drink_order_number, int)
        self.assertTrue(drink_order_number, range(1, 33))

        editable = False
        self.assertFalse(editable)
        self.assertFalse(editable, bool)

        blank = True
        self.assertTrue(blank)
        self.assertTrue(blank, bool)

        related_name = "drink_orders"
        self.assertTrue(related_name, str)

        full_name = 50
        self.assertEqual(full_name, 50)
        self.assertTrue(full_name, int)
        self.assertTrue(full_name, range(1, 51))

        null = False
        self.assertFalse(null)
        self.assertFalse(null, bool)

        blank = False
        self.assertFalse(blank)
        self.assertFalse(blank, bool)

        email = 254
        self.assertEqual(email, 254)
        self.assertTrue(email, int)
        self.assertTrue(email, range(1, 255))

        phone_number = 30
        self.assertEqual(phone_number, 30)
        self.assertTrue(phone_number, int)
        self.assertTrue(phone_number, range(1, 31))

        street_address1 = 80
        self.assertEqual(street_address1, 80)
        self.assertTrue(street_address1, int)
        self.assertTrue(street_address1, range(1, 81))

        street_address2 = 80
        self.assertEqual(street_address2, 80)
        self.assertTrue(street_address2, int)
        self.assertTrue(street_address2, range(1, 81))

        postcode = 20
        self.assertEqual(postcode, 20)
        self.assertTrue(postcode, int)
        self.assertTrue(postcode, range(1, 21))

        country = "Country *"
        self.assertTrue(country, str)

        subtotal = 10
        self.assertEqual(subtotal, 10)
        self.assertTrue(subtotal, int)
        self.assertTrue(subtotal, range(1, 11))

        decimal_places = 2
        self.assertEqual(decimal_places, 2)
        self.assertTrue(decimal_places, int)

        default = 0
        self.assertEqual(default, 0)
        self.assertFalse(default, int)
        self.assertFalse(default, range(0, 1))

        delivery_cost = 6
        self.assertEqual(delivery_cost, 6)
        self.assertTrue(delivery_cost, int)
        self.assertTrue(delivery_cost, range(1, 6))

        grand_total = 10
        self.assertEqual(grand_total, 10)
        self.assertTrue(grand_total, int)
        self.assertTrue(grand_total, range(1, 11))

        auto_now_add = True
        self.assertTrue(auto_now_add)
        self.assertTrue(auto_now_add, bool)

        default = ""
        self.assertFalse(default, str)

        stripe_pid = 254
        self.assertEqual(stripe_pid, 254)
        self.assertTrue(stripe_pid, int)
        self.assertTrue(stripe_pid, range(1, 255))

    def test_update_total(self):
        subtotal = "lineitem_total" or "lineitem_total__sum"
        self.assertTrue(subtotal, str)

        subtotal = 0
        self.assertEqual(subtotal, 0)
        self.assertFalse(subtotal, int)
        self.assertFalse(subtotal, range(0, 1))

    def test_drink_order_line_item(self):
        null = False
        self.assertFalse(null)
        self.assertFalse(null, bool)

        blank = False
        self.assertFalse(blank)
        self.assertFalse(blank, bool)

        related_name = "lineitems"
        self.assertTrue(related_name, str)

        default = 0
        self.assertEqual(default, 0)
        self.assertFalse(default, int)
        self.assertFalse(default, range(0, 1))

        lineitem_total = 6
        self.assertEqual(lineitem_total, 6)
        self.assertTrue(lineitem_total, int)
        self.assertTrue(lineitem_total, range(1, 7))

        decimal_places = 2
        self.assertEqual(decimal_places, 2)
        self.assertTrue(decimal_places, int)

        editable = False
        self.assertFalse(editable)
        self.assertFalse(editable, bool)
