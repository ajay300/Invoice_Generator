from rest_framework import serializers
from app.models import Product ,Customer



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['title','product_pic','description','price','quantity']

        # def validate_s(self , value):
        
        #     if value >= 20 or value == 15:
        #         raise serializers.ValidationError('selt full')
        #     return value

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['name','address','phone']
