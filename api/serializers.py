

import re
from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField, SlugRelatedField, StringRelatedField
from .models import ParametersItem, Product, Parameter


class ParameterSerializer(SlugRelatedField,serializers.ModelSerializer):

    class Meta:
        model = Parameter
        

class ProductSerializer(serializers.ModelSerializer):
    parameter = ParameterSerializer(many=True, queryset=Parameter.objects.all(), slug_field='title')
    
    class Meta:
        model = Product
        fields = ("product_title", "description", "parameter",)
        