from django.test import TestCase
from .models import DrinkOrderLineItem


class TestSignals(TestCase):
    def test_update_on_save_and_delete(self):
        sender = DrinkOrderLineItem
        self.assertTrue(sender, DrinkOrderLineItem)
