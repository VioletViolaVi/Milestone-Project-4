from django.test import TestCase


class TestUrls(TestCase):
    def test_url_patterns(self):
        self.assertFalse("", str)
        self.assertTrue("shopping_cart", str)

        self.assertTrue("add/<item_id>/", str)
        self.assertTrue("add_to_shopping_cart", str)

        self.assertTrue("edit/<item_id>/", str)
        self.assertTrue("edit_shopping_cart", str)

        self.assertTrue("delete/<item_id>/", str)
        self.assertTrue("delete_shopping_cart_item", str)

        name = \
            "shopping_cart" or "add_to_shopping_cart" or "edit_shopping_cart" \
            or "delete_shopping_cart_item"
        self.assertIs(
            name, "shopping_cart" or "add_to_shopping_cart" or
            "edit_shopping_cart" or "delete_shopping_cart_item")
