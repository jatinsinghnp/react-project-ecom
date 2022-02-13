from django.shortcuts import render
from shop.models import Product
from rest_framework.generics import ListAPIView
from .serializer import ProductSerilizers

# Create your views here.


class ApiHome(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerilizers
