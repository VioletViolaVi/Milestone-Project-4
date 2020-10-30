from django import forms
from .widgets import CustomClearableFileInput
from .models import Drink, Drink_type, About_us, About_us_part


class DrinkForm(forms.ModelForm):

    class Meta:
        model = Drink
        fields = "__all__"

    image = forms.ImageField(widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        drink_types = Drink_type.objects.all()
        friendly_names = [(
            drink.id, drink.get_friendly_name()) for drink in drink_types]

        self.fields["drink_type"].choices = friendly_names


class AboutUsForm(forms.ModelForm):

    class Meta:
        model = About_us
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        about_us_parts = About_us_part.objects.all()
        friendly_names = [(
            about.id, about.get_friendly_name()) for about in about_us_parts]

        self.fields["about_us_sections"].choices = friendly_names
