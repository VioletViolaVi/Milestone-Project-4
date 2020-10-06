from django.contrib import admin
from .models import Drink_type, Drink

# registers models to admin
admin.site.register(Drink_type)
admin.site.register(Drink)
