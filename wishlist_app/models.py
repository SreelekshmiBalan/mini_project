from django.db import models
from products_app.models import Product
from user_accounts_app.models import Account

# Create your models here.

class WishLists(models.Model):
    user=models.ForeignKey(Account,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    added_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together=('user','product')

    def __str__(self):
        return self.product.Name

