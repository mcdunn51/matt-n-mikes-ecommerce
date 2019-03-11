from django.contrib import admin
from django.contrib.auth.models import User
from django.urls import include, path
from oauth2_provider.contrib.rest_framework import (TokenHasReadWriteScope, TokenHasScope)
from rest_framework import generics, permissions, serializers
from api.models import Product
# from serializers import ProdListSerializer, ProdDetailedSerializer
admin.autodiscover()

from oauth2_provider.decorators import protected_resource


# first we define the serializers
class ProdListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "itemno", "description", "price",)

class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "itemno", "description", "description2", "price", "colour", "manufacturerCode")

# Create the API views

class Productlist(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = Product.objects.all()
    serializer_class = ProdListSerializer
    def get(self, request, *args, **kwargs):
        if 'manufacturerCode' in self.request.query_params:
            if len(self.request.query_params['manufacturerCode']) > 0:
                self.queryset = self.queryset.filter(manufacturerCode=self.request.query_params['manufacturerCode'])
        if 'itemno' in self.request.query_params:
            if len(self.request.query_params['itemno']) > 0:
                self.queryset = self.queryset.filter(itemno=self.request.query_params['itemno'])
        if 'LTPrice' in self.request.query_params:
            if len(self.request.query_params['LTPrice']) > 0:
                self.queryset = self.queryset.filter(price__lte=self.request.query_params['LTPrice'])
        if 'GTPrice' in self.request.query_params:
            if len(self.request.query_params['GTPrice']) > 0:
                self.queryset = self.queryset.filter(price__gte=self.request.query_params['GTPrice'])
        return super().get(request, *args, **kwargs)

class Manufacturerlist(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = Product.objects.all()
    serializer_class = ProdListSerializer
    def get(self, request, *args, **kwargs):
        self.queryset = Product.objects.filter(manufacturerCode=self.request.query_params['manufacturerCode'])
        return super().get(request, *args, **kwargs)

# Setup the URLs and include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('Productlist/', Productlist.as_view()),
    path('Manufacturer/', Productlist.as_view()),
    
]