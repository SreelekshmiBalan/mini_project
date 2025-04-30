from django.db import models
from products_app.models import Product

# Create your models here.
# class WishList(models.Model):
#     product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True,blank=True)
#     Product_Name=models.CharField(max_length=250)
#     Product_Code=models.CharField(max_length=100)
#     Product_Price=models.IntegerField()
#     def __str__(self):
#         return self.product.Name

