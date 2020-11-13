from django.test import TestCase


class TestWidgets(TestCase):

    def test_custom_clearable_file_input(self):
        template_name = \
            "about_us/custom_widget_templates/custom_clearable_file_input.html"
        self.assertTrue(
            template_name,
            "about_us/custom_widget_templates/\
                custom_clearable_file_input.html")
