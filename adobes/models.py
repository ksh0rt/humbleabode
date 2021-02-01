from django.db import models

class Abode(models.Model):
    price = models.IntegerField()
    address = models.CharField(max_length=255)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    SqFoot = models.IntegerField()
    image = models.ImageField(upload_to='humbleabode/images/')
