from django.test import TestCase


class TestApps(TestCase):

    def test_drinks_config(self):
        name = "home"
        self.assertIs(name, "home")
