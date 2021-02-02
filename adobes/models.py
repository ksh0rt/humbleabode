from django.db import models
from django.contrib.auth.models import User

class Abode(models.Model):
    price = models.IntegerField()
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=20) #Longest city name in the US is 17 characters
    state = models.CharField(max_length=2) #Two for state abbreviations
    zip_code = models.CharField(max_length=5) #Zipcodes are 5 digits long
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    SqFoot = models.IntegerField()
    image = models.ImageField(upload_to='humbleabode/images/', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
