from django import forms
from .models import DrinkOrder


class DrinkOrderForm(forms.ModelForm):
    class Meta:
        model = DrinkOrder
        fields = ("full_name", "email", "phone_number",
                  "street_address1", "street_address2", "postcode",
                  "country",)

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        placeholders = {
            "full_name": "Full Name",
            "email": "Email",
            "phone_number": "Phone Number",
            "street_address1": "Street Address 1",
            "street_address2": "Street Address 2",
            "postcode": "Postal Code",
            "country": "Country",
        }

        self.fields["full_name"].widget.attrs["autofocus"] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f"{placeholders[field]} *"
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs["placeholder"] = placeholder
            self.fields[field].widget.attrs["class"] = "stripe-style-input"
            self.fields[field].label = False
