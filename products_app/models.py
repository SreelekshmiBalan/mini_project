from django.db import models

# Create your models here.
class Category(models.Model):
    Category_Name=models.CharField(max_length=500)
    Category_Image=models.ImageField(upload_to='category_images/', blank=True, null=True)
    Category_Description=models.CharField(max_length=2000)
    Top_Category=models.BooleanField(default=False)
    def __str__(self):
        return self.Category_Name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    Name=models.CharField(max_length=500)
    Product_Code=models.CharField(max_length=100,null=True,blank=True)
    Price=models.IntegerField(null=True,blank=True)
    Colour=models.CharField(max_length=1000,null=True,blank=True)
    Material=models.CharField(max_length=1000,null=True,blank=True)
    Type=models.CharField(max_length=1000,null=True,blank=True)
    Wash_Care=models.CharField(max_length=1000,null=True,blank=True)
    Stock=models.CharField(max_length=100) 
    Availability=models.CharField(max_length=100)
    Best_Seller=models.BooleanField(default=False)
    New_Launch=models.BooleanField(default=False)
    def __str__(self):
        return self.Name

class ProductImage(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='images')
    Image=models.FileField(upload_to='product_images/', blank=True, null=True)
    def __str__(self):
        return self.product.Name



    