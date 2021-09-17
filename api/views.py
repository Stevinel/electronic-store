from django.shortcuts import render
from rest_framework import generics
from .models import Parameter, Product
from .serializers import ProductSerializer
from django_filters import rest_framework as filters
from django.http import JsonResponse


class MyFilterBackend(filters.DjangoFilterBackend):
    def get_filterset_kwargs(self, request, queryset, view):
        kwargs = super().get_filterset_kwargs(request, queryset, view)
        print(kwargs)
        if "parameter" in request.GET:
            parameter = request.GET['parameter']
            queryset = Product.objects.all().filter(parameter__title=parameter)
            
        return kwargs

class ProductGetPost(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (MyFilterBackend,)
    # filterset_fields = ('id', 'product_title', 'parameter__title')


