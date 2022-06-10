from itertools import product
from django.contrib import admin
from .models import Customer , Product ,Seller
# Register your models here.


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name','address','phone']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','description','price']

@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ['name','address','email','phone']