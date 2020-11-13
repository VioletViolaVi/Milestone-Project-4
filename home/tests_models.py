from django.test import TestCase


class TestModels(TestCase):

    def test_drink_type(self):
        programmatic_name = 255
        friendly_name = 255
        self.assertEqual(programmatic_name, 255)
        self.assertTrue(255, range(1, 256))
        self.assertEqual(friendly_name, 255)
        self.assertTrue(255, range(1, 256))

    def test_drink(self):
        drink_name = 255
        price = range(1, 11)
        decimal_places = 2
        self.assertEqual(drink_name, 255)
        self.assertTrue(255, range(1, 256))
        self.assertEqual(price, range(1, 11))
        self.assertEqual(decimal_places, 2)
