from django_filters import FilterSet
from .models import Product

class ProductFilter(FilterSet):
    class Meta:
        model = Product
        fields = {
            'have': ['exact'],
            'price':['gt', 'lt'],
            'created_date': ['gt', 'lt']
        }

