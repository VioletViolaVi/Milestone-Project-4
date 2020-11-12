from django import forms
from .widgets import CustomClearableFileInput
from .models import About_us, About_us_section


class AboutUsForm(forms.ModelForm):

    class Meta:
        model = About_us
        fields = "__all__"

    image = forms.ImageField(widget=CustomClearableFileInput, required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        about_us_sections = About_us_section.objects.all()
        friendly_names = [(
            a.id, a.get_friendly_name()) for a in about_us_sections]

        self.fields["section"].choices = friendly_names
