from distutils.command import upload
from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.


class Customer(models.Model):
    
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    phone = models.IntegerField()
    
    # date = models.DateTimeField(auto_now=True)


class Product(models.Model):
    title = models.CharField(max_length=100)
    product_pic = models.ImageField(upload_to="product_img")
    description = models.CharField(max_length=200)
    price = models.FloatField()
    quantity = models.PositiveIntegerField()




class Seller(models.Model):
    
    name = models.CharField(max_length=50,default="Virtual Company Ltd.")
    address = models.CharField(max_length=150,default="23th Street, Zbcxyz")
    phone = models.IntegerField(default='+91 900XX XX XXX')
    email = models.CharField(max_length=150 , default="abc@xompany.com")
    # date = models.DateField(default=datetime.datetime.date)
