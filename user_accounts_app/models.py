from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Account(AbstractUser):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True) 
    phone = models.CharField(max_length=15, null=True, blank=True)  
    address_line_1 = models.CharField(max_length=500, null=True, blank=True)
    address_line_2 = models.CharField(max_length=500, null=True, blank=True)
    district = models.CharField(max_length=255,null=True,blank=True)
    state = models.CharField(max_length=255,null=True,blank=True)
    pin_code = models.IntegerField(null=True, blank=True)  
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.username if self.username else "Unnamed User"
    


# class Account(models.Model):
#     First_Name=models.CharField(max_length=500)
#     Last_Name=models.CharField(max_length=500)
#     Gender=models.CharField(max_length=500)
#     Birth_Date=models.CharField(max_length=500,null=True,blank=True)
#     Email=models.CharField(max_length=500)
#     Phone=models.IntegerField(null=True,blank=True)
#     AddressLine1=models.CharField(max_length=500)
#     AddressLine2=models.CharField(max_length=500)
#     District=models.CharField(max_length=500)
#     State=models.CharField(max_length=500)
#     PINCode=models.IntegerField(null=True,blank=True)
#     Username=models.CharField(max_length=500)
#     Password=models.CharField(max_length=500)
#     ConfirmPSW=models.CharField(max_length=500)

