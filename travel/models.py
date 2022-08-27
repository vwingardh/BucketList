from django.db import models

ADVENTURE_CHOICES = (
    ('beach', 'Beach'),
    ('diving', 'Diving'),
    ('city', 'City'),
    ('hiking', 'Hiking'),
)

CLIMATE_CHOICES = (
    ('tropical', 'Tropical'),
    ('cold', 'Cold'),
    ('temperate', 'Temperate'),
)

FLIGHT_CHOICES = (
    ('short', 'Short'),
    ('long', 'Long'),
)

class Destination(models.Model):
    city = models.CharField('City', max_length=50)
    country = models.CharField('Country', max_length=50)
    adventure = models.CharField('Adventure', max_length=20, choices = ADVENTURE_CHOICES)
    climate = models.CharField('Climate', max_length=50, choices = CLIMATE_CHOICES)
    flight = models.CharField('Flight Length', max_length=50, choices = FLIGHT_CHOICES)
    image = models.ImageField('Image', null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.city


class Checkoff(models.Model):
    city = models.CharField('City', max_length=50)
    country = models.CharField('Country', max_length=50)
    adventure = models.CharField('Adventure', max_length=20, choices = ADVENTURE_CHOICES)
    climate = models.CharField('Climate', max_length=50, choices = CLIMATE_CHOICES)
    flight = models.CharField('Flight Length', max_length=50, choices = FLIGHT_CHOICES)
    image = models.ImageField('Image', null=True, blank=True, upload_to="media/images/")

    def __str__(self):
        return self.city


class Next(models.Model):
    adventure = models.CharField('Type of Adventure', max_length=20, choices = ADVENTURE_CHOICES)
    climate = models.CharField('Climate', max_length=50, choices = CLIMATE_CHOICES)
    flight = models.CharField('Flight Length', max_length=50, choices = FLIGHT_CHOICES)

    def __str__(self):
        return self.adventure