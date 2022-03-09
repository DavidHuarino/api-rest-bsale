from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

class Product(models.Model):
    name = models.CharField(max_length=50)
    url_image = models.CharField(max_length=200)
    price = models.FloatField()
    discount = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

