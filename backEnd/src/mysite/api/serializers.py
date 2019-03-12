from rest_framework import serializers
from .models import Product, Address

class ProdListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "itemno", "description", "price",)

class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "manufacturerCode")

class AdressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ("customerID", "address1", "address2", "town", "county", "postcode", "phoneNumber", "email", "country")