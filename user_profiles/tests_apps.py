from django.test import TestCase


class TestApps(TestCase):

    def test_user_profiles_config(self):
        name = "user_profiles"
        self.assertIs(name, "user_profiles")
        self.assertTrue(name, str)
