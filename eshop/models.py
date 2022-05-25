from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=300)

    def __str__(self):
        return self.title

class Product(models.Model):
    product_name = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    price = models.FloatField()
    stock = models.IntegerField()
    image1 = models.ImageField(upload_to='products/')
    image2 = models.ImageField(upload_to='products/')
    image3 = models.ImageField(upload_to='products/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


