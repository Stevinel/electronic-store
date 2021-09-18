from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from .models import Parameter, Product


class ParameterSerializer(SlugRelatedField, serializers.ModelSerializer):
    class Meta:
        model = Parameter
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    parameter = ParameterSerializer(
        many=True, queryset=Parameter.objects.all(), slug_field="title"
    )

    class Meta:
        model = Product
        fields = (
            "product_title",
            "description",
            "parameter",
        )
