from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters

from .models import Product
from .serializers import ProductSerializer


class ProductGetPost(generics.ListCreateAPIView):
    """
    Функция создания нового товара с
    возможностью фильтрации по id, параметрам, названию и поиском по названию.
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ("id", "parameter", "product_title")
    search_fields = ("^product_title",)
