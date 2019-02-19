from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    description2 = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20, default=0.00)
    colour = models.CharField(max_length=50)
    def __str__(self):
        return self.title