from django.db import models

# Create your models here.

class Account(models.Model):
    First_Name=models.CharField(max_length=500)
    Last_Name=models.CharField(max_length=500)
    Gender=models.CharField(max_length=500)
    Birth_Date=models.CharField
    Email=models.CharField(max_length=500)
    Phone=models.IntegerField
    AddressLine1=models.CharField(max_length=500)
    AddressLine2=models.CharField(max_length=500)
    District=models.CharField(max_length=500)
    State=models.CharField(max_length=500)
    PINCode=models.IntegerField()
    Username=models.CharField(max_length=500)
    Password=models.CharField(max_length=500)

