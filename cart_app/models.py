from django.db import models
from user_accounts_app.models import Account
from products_app.models import Product
from django.core.exceptions import ValidationError


# Create your models here.

class Cart(models.Model):
    user=models.ForeignKey(Account,on_delete=models.CASCADE,null=True,blank=True)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    size=models.CharField(max_length=50)
    quantity=models.IntegerField(default=1)
    def clean(self):
        if not self.user:
            raise ValidationError("Cart item must be associated with a logged-in user.")
    def __str__(self):
        return self.product.Name