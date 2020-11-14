from django.test import TestCase


class TestViews(TestCase):

    def test_user_profiles(self):
        self.assertTrue("POST", str)

        self.assertTrue("Your profile has successfully updated!", str)
        self.assertTrue("Update failed. Please ensure the form is valid.", str)

        self.assertTrue("user_profiles/user_profiles.html", str)

        self.assertTrue("form", str)
        self.assertTrue("drink_orders", str)

    def test_drink_order_history(self):

        self.assertTrue("payment/payment_success.html", str)
        self.assertTrue("drink_order", str)
        self.assertTrue("taken_from_user_profiles", str)

    def test_go_to_user_profiles_page(self):
        response = self.client.get("/accounts/login/?next=/user_profiles/")
        self.assertEqual(response.status_code, 200)

    def test_go_to_drink_order_history_page(self):
        response = self.client.get(
            "/accounts/login/?next=/user_profiles/drink_order_history/")
        self.assertEqual(response.status_code, 200)
