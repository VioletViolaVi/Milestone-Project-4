from django.db import models


class Drink_type(models.Model):
    programmatic_name = models.CharField(max_length=300)
    friendly_name = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.programmatic_name

    def get_friendly_name(self):
        return self.friendly_name


class Drink(models.Model):
    drink_type = models.ForeignKey("Drink_type", null=True, blank=True, on_delete=models.SET_NULL)
    image = models.ImageField()
    drink_name = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    millilitres = models.IntegerField()
    image_name = models.CharField(max_length=300, null=True, blank=True)
    url = models.URLField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.drink_name
