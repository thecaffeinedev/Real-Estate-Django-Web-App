from django.db import models

# Create your models here.
class Listing(models.model):
    realtor = models.ForeignKey("Realtor", on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    title = models.models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.models.IntegerField()
    bathrooms = models.models.DecimalField(max_digits=2, decimal_places=2)
    grarage = models.IntegerField(default = 0 )
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=2, decimal_places=2)
    photo_main = models.ImageField( upload_to='photos/%Y%m/%d')
