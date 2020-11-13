from django.test import TestCase


class TestAdmin(TestCase):

    def test_drink_order_line_Item_admin_inline(self):
        self.assertTrue("lineitem_total", str)
        readonly_fields = ("lineitem_total",)
        self.assertTrue(readonly_fields, tuple)

    def test_drink_order_admin(self):
        readonly_fields = ("drink_order_number", "date",
                           "delivery_cost", "subtotal",
                           "grand_total",
                           "original_shopping_cart",
                           "stripe_pid")

        fields = ("drink_order_number", "full_name",
                  "user_profiles", "email",
                  "phone_number", "street_address1",
                  "street_address2", "postcode",
                  "country", "subtotal",
                  "delivery_cost", "grand_total",
                  "date", "original_shopping_cart",
                  "stripe_pid")

        list_display = ("drink_order_number", "date",
                        "full_name", "subtotal",
                        "delivery_cost", "grand_total",)

        ordering = ("-date",)
        self.assertTrue(readonly_fields, tuple)
        self.assertTrue(fields, tuple)
        self.assertTrue(list_display, tuple)
        self.assertTrue(ordering, tuple)
