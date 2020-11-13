from django.test import TestCase


class TestAdmin(TestCase):

    def test_about_us_section_admin(self):
        list_display = ("programmatic_name", "friendly_name")
        self.assertIs(list_display, ("programmatic_name", "friendly_name"))
        self.assertTrue(list_display, tuple)

    def test_about_us_admin(self):
        list_display = ("title", "paragraph", "section",
                        "image", "image_description",)
        self.assertIs(list_display, ("title", "paragraph", "section",
                                     "image", "image_description",))
        self.assertTrue(list_display, tuple)
