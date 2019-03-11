from rest_framework import serializers
from api.model import Product

class ProdListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "itemno", "description", "price",)

class ProdDetailedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "itemno", "description", "description2", "price", "colour", "manufacturerCode")