from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from decimal import *

class Abode(models.Model):
    price = models.PositiveIntegerField(default=100000)
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=20) #Longest city name in the US is 17 characters
    state = models.CharField(max_length=2) #Two for state abbreviations
    zip_code = models.CharField(max_length=5) #Zipcodes are 5 digits long
    bedrooms = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])
    bathrooms = models.DecimalField(max_digits=3, decimal_places=1, validators=[MinValueValidator(Decimal('0.5'))])
    SqFoot = models.PositiveIntegerField(default=100, validators=[MinValueValidator(1)])
    image = models.ImageField(upload_to='humbleabode/images/', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
