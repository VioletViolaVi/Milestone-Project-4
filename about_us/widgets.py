from django.forms.widgets import ClearableFileInput


class CustomClearableFileInput(ClearableFileInput):
    template_name = \
        "about_us/custom_widget_templates/custom_clearable_file_input.html"
