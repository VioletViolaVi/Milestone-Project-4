from django import forms
from .models import Drink, Drink_type


class DrinkForm(forms.ModelForm):

    class Meta:
        model = Drink
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        drink_types = Drink_type.objects.all()
        friendly_names = [(
            drink.id, drink.get_friendly_name()) for drink in drink_types]

        self.fields["drink_type"].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "border-black rounded-0"
