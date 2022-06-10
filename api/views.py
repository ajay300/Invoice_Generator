from django.shortcuts import render

# Create your views here.
from app.models import Product , Customer
from .serializers import ProductSerializer , CustomerSerializer
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateAPIView , RetrieveDestroyAPIView 
# ListAPIView , CreateAPIView , RetrieveAPIView , UpdateAPIView , DestroyAPIView , 

# from app import serializers


# Concrete View : ListAPIView + UpdateAPIView = ListCreateview 
class ProductListcreate(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductRetrieveUpdate(RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductRetrieveDestroy(RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# customer 

class CustomerListcreate(ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerRetrieveUpdate(RetrieveUpdateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerRetrieveDestroy(RetrieveDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer



# ------------------------------- GenericAPIView + ListModelMixin = ListAPIView --------------------------------------------

# class StudentList(ListAPIView):
#     queryset = Students.objects.all()
#     serializer_class = StudentSerializer

# class Studentcreate(CreateAPIView):
#     queryset = Students.objects.all()
#     serializer_class = StudentSerializer

# class StudentRetrieve(RetrieveAPIView):
#     queryset = Students.objects.all()
#     serializer_class = StudentSerializer

# class StudentUdpate(UpdateAPIView):
#     queryset = Students.objects.all()
#     serializer_class = StudentSerializer

# class StudentDestroy(DestroyAPIView):
#     queryset = Students.objects.all()
#     serializer_class = StudentSerializer











# I am writing to let you know that I will be unable to meet the deadline for the project you assigned to me last week. 