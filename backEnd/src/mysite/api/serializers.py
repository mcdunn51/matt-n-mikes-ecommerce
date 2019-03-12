from rest_framework import serializers
from .models import Product

class ProdListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "itemno", "description", "price",)

class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "manufacturerCode")