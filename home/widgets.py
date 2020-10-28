from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _


class CustomClearableFileInput(ClearableFileInput):
    input_text = _("")
    template_name = \
        "home/custom_widget_templates/custom_clearable_file_input.html"
