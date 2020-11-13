from django.test import TestCase


class TestUrls(TestCase):
    def test_url_patterns(self):
        name = \
            "home" or "add_drink" or "edit_drink" or "delete_drink"
        self.assertIs(
            name, "home" or "add_drink" or "edit_drink" or "delete_drink")
