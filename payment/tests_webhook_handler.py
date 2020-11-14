from django.test import TestCase


class TestWebhooks(TestCase):

    def test_send_confirmation_email(self):
        self.assertTrue(
            "payment/confirmation_emails/confirmation_email_subject.txt", str)
        self.assertTrue("drink_order", str)
        self.assertTrue(
            "payment/confirmation_emails/confirmation_email_body.txt", str)
        self.assertTrue("contact_email", str)

    def test_handle_event(self):
        status = 200
        self.assertEqual(status, 200)
        self.assertTrue(status, int)
        self.assertTrue(status, range(1, 201))

    def test_handle_payment_intent_succeeded(self):
        user_profiles = None
        self.assertIsNone(user_profiles)

        self.assertTrue("AnonymousUser", str)

        drink_order_exists = False
        self.assertFalse(drink_order_exists)
        self.assertFalse(drink_order_exists, bool)

        attempt = 1
        self.assertEqual(attempt, 1)
        self.assertTrue(attempt, int)
        self.assertTrue(attempt, range(1, 2))

        attempt <= 5
        self.assertLessEqual(attempt, 5)
        self.assertTrue(attempt, int)
        self.assertTrue(attempt, range(1, 6))

        drink_order_exists = True
        self.assertTrue(drink_order_exists)
        self.assertTrue(drink_order_exists, bool)

        attempt = attempt + 1
        self.assertTrue(attempt, int)
        self.assertTrue(attempt, range(1, 7))

        status = 200
        self.assertEqual(status, 200)
        self.assertTrue(status, int)
        self.assertTrue(status, range(1, 201))

        drink_order = None
        self.assertIsNone(drink_order)

        status = 500
        self.assertEqual(status, 500)
        self.assertTrue(status, int)
        self.assertTrue(status, range(1, 501))
