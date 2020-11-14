from django.test import TestCase


class TestModels(TestCase):

    def test_drink_type(self):
        programmatic_name = 255
        self.assertEqual(programmatic_name, 255)
        self.assertTrue(programmatic_name, range(1, 256))
        self.assertTrue(programmatic_name, int)
        friendly_name = 255
        self.assertEqual(friendly_name, 255)
        self.assertTrue(friendly_name, range(1, 256))
        self.assertTrue(friendly_name, int)
        null = True
        self.assertTrue(null)
        self.assertTrue(null, bool)
        blank = True
        self.assertTrue(blank)
        self.assertTrue(blank, bool)

    def test_drink(self):
        drink_name = 255
        self.assertEqual(drink_name, 255)
        self.assertTrue(drink_name, range(1, 256))
        self.assertTrue(drink_name, int)
        price = 10
        self.assertEqual(price, 10)
        self.assertTrue(price, range(1, 11))
        self.assertTrue(price, int)
        decimal_places = 2
        self.assertEqual(decimal_places, 2)
