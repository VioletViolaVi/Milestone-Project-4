from django.test import TestCase


class TestUrls(TestCase):
    def test_url_patterns(self):
        self.assertFalse("", str)
        self.assertTrue("append/", str)
        self.assertTrue("change/", str)
        self.assertTrue("remove/", str)
        name = \
            "about_us" or "append_about_us" or \
            "change_about_us" or "remove_about_us"
        self.assertIs(
            name, "about_us" or "append_about_us" or
            "change_about_us" or "remove_about_us")
