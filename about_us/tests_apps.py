from django.test import TestCase


class TestApps(TestCase):

    def test_about_us_config(self):
        name = "about_us"
        self.assertIs(name, "about_us")
