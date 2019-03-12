from django.db import models

# Create your models here.

class Product(models.Model):
    itemno = models.CharField(max_length=120)
    description = models.TextField()
    description2 = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20, default=0.00)
    colour = models.CharField(max_length=50)
    manufacturerCode = models.CharField(max_length = 50)
    def __str__(self):
        return self.itemno

class Address(models.Model):
    customerID = models.IntegerField()
    address1 = models.CharField(max_length=20)
    address2 = models.CharField(max_length=20)
    town = models.CharField(max_length=20)
    county = models.CharField(max_length=20)
    postcode = models.CharField(max_length=20)
    phoneNumber = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    def __str__(self):
        return self.address1
