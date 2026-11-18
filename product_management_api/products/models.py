from django.db import models

# Create your models here.
class Product(models.Model):
    product_name=models.CharField(max_length=20)
    product_code=models.CharField(max_length=20)
    category=models.CharField(max_length=20)
    price=models.IntegerField()
    stock_quantity=models.IntegerField()
    image=models.ImageField(upload_to='products',null=True)
