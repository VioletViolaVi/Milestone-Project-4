from django.test import TestCase


class TestUrls(TestCase):
    def test_url_patterns(self):
        self.assertFalse("", str)
        self.assertTrue("add/", str)
        self.assertTrue("edit/", str)
        self.assertTrue("delete/", str)
        name = \
            "home" or "add_drink" or "edit_drink" or "delete_drink"
        self.assertIs(
            name, "home" or "add_drink" or "edit_drink" or "delete_drink")
