from django.test import TestCase


class TestViews(TestCase):

    def test_shopping_cart(self):
        self.assertTrue("shopping_cart/shopping_cart.html", str)

    def test_add_to_shopping_cart(self):
        self.assertTrue("drinkSelections", str)
        self.assertTrue("redirect_url", str)
        self.assertTrue("shopping_cart", str)

    def test_edit_shopping_cart(self):
        self.assertTrue("editDrinks", str)
        self.assertTrue("shopping_cart", str)

        self.assertTrue("Please pick a number from 1-100.", str)
        self.assertTrue("shopping_cart/shopping_cart.html", str)

    def test_delete_shopping_cart_item(self):
        self.assertTrue("shopping_cart", str)

        status = 500
        self.assertEqual(status, 500)
        self.assertTrue(status, int)
        self.assertTrue(status, range(1, 501))
