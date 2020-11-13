from django.test import TestCase


class TestWidgets(TestCase):

    def test_custom_clearable_file_input(self):
        template_name = \
            "home/custom_widget_templates/custom_clearable_file_input.html"
        self.assertIs(
            template_name,
            "home/custom_widget_templates/custom_clearable_file_input.html")
