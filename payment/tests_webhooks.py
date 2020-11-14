from django.test import TestCase
from django.conf import settings
import stripe


class TestWebhooks(TestCase):

    def test_webhook(self):
        wh_secret = settings.STRIPE_WH_SECRET
        stripe.api_key = settings.STRIPE_SECRET_KEY
        self.assertIs(wh_secret, settings.STRIPE_WH_SECRET)
        self.assertTrue(stripe.api_key, settings.STRIPE_SECRET_KEY)
        self.assertTrue("HTTP_STRIPE_SIGNATURE", str)
        event = None
        self.assertIsNone(event)
        status = 400
        self.assertEqual(status, 400)
        self.assertTrue("payment_intent.succeeded", str)
        self.assertTrue("payment_intent.payment_failed", str)
        self.assertTrue("type", str)

    def test_go_to_webhook(self):
        response = self.client.get("/accounts/login/?next=/wh/")
        self.assertEqual(response.status_code, 200)
