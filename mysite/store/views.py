from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['have', 'price']
    search_fields = ['product_name']
    ordering_fields = ['price', 'created_date']