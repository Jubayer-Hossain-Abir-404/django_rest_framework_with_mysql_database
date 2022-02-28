from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    category = models.CharField(max_length=100, null=False, blank=False)
    # here 2 deciaml places means 50.35
    price = models.DecimalField(max_digits=4, decimal_places=2)
    # it takes text inputs
    description = models.TextField()
    # it takes integer field
    stars = models.IntegerField()

    # it is known as dunder method
    def __str__(self):
        # it is returning the prodect name
        return self.name

