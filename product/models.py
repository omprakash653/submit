from django.db import models

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=50)
    weight = models.IntegerField()
    price = models.IntegerField(default=0)
    date = models.DateField(auto_now=True)


    def __str__(self):
        return self.product_name
    