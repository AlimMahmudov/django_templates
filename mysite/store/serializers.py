from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name']

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    created_date = serializers.DateTimeField(format='%d-%m-%Y %H:%M')
    class Meta:
        model = Product
        fields = ['product_name', 'descrioption', 'category', 'price', 'created_date', 'image', 'video']