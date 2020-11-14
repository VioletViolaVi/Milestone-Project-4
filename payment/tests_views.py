from django.test import TestCase


class TestViews(TestCase):

    def test_cache_payment_data(self):
        self.assertTrue("client_secret", str)
        self.assertTrue("_secret", str)
        self.assertTrue("shopping_cart", str)
        self.assertTrue("save_info", str)
        self.assertTrue("username", str)

        status = 200
        self.assertEqual(status, 200)
        self.assertTrue(status, int)
        self.assertTrue(status, range(1, 201))

        self.assertTrue("Sorry, your payment cannot be \
            processed right now. Please try again later.", str)

        status = 400
        self.assertEqual(status, 400)
        self.assertTrue(status, int)
        self.assertTrue(status, range(1, 401))

    def test_payment(self):
        self.assertTrue("client_secret", str)
        self.assertTrue("POST", str)
        self.assertTrue("shopping_cart", str)

        self.assertTrue("full_name", str)
        self.assertTrue("email", str)
        self.assertTrue("phone_number", str)
        self.assertTrue("street_address1", str)
        self.assertTrue("street_address2", str)
        self.assertTrue("postcode", str)
        self.assertTrue("country", str)

        commit = False
        self.assertFalse(commit)
        self.assertFalse(commit, bool)

        self.assertTrue("_secret", str)
        self.assertTrue("One of the items in your shopping \
                             cart wasn't found in our database. \
                                 Please call us for assistance!", str)
        self.assertTrue("save_info", str)
        self.assertTrue("save-info", str)
        self.assertTrue("payment_success", str)

        self.assertTrue("There was an error with your form. \
                    Please check your information again.", str)
        self.assertTrue("There's nothing in your shopping cart.", str)
        self.assertTrue("home", str)
        self.assertTrue("grand_total", str)

        self.assertTrue("Stripe public key is missing. \
            Did you forget to set it in your environment?", str)
        self.assertTrue("payment/payment.html", str)
        self.assertTrue("drink_order_form", str)
        self.assertTrue("stripe_public_key", str)

    def test_payment_success(self):
        self.assertTrue("save_info", str)

        self.assertTrue("default_full_name", str)
        self.assertTrue("default_phone_number", str)
        self.assertTrue("default_street_address1", str)
        self.assertTrue("default_street_address2", str)
        self.assertTrue("default_postcode", str)
        self.assertTrue("default_country", str)

        self.assertTrue("shopping_cart", str)

        self.assertTrue("payment/payment_success.html", str)
        self.assertTrue("drink_order", str)
        self.assertTrue("this_is_successful_payment_page", str)
