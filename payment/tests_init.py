from django.test import TestCase


class Test_init(TestCase):
    def test_init_py(self):
        default_app_config = "payment.apps.PaymentConfig"
        self.assertTrue(default_app_config, str)
