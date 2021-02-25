from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from decimal import *

class Address(models.Model):
    address_id = models.AutoField(primary_key=True)
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=20) #Longest city name in the US is 17 characters
    state = models.CharField(max_length=2) #Two for state abbreviations
    zip_code = models.CharField(max_length=5) #Zipcodes are 5 digits long

class Abode(models.Model):
    price = models.PositiveIntegerField(default=100000)
    bedrooms = models.PositiveIntegerField(verbose_name='Bedrooms:',default=1, validators=[MinValueValidator(1)])
    bathrooms = models.DecimalField(verbose_name='Bathrooms:',max_digits=3, decimal_places=1, validators=[MinValueValidator(Decimal('0.5'))])
    SqFoot = models.PositiveIntegerField(verbose_name='Square Feet:',default=100, validators=[MinValueValidator(1)])
    image = models.ImageField(upload_to='humbleabode/images/', blank=True)
    is_sold = models.BooleanField(default=False, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
