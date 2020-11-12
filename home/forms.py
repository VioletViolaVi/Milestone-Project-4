from django import forms
from .widgets import CustomClearableFileInput
from .models import Drink, Drink_type


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
