from django.contrib import admin
from django.contrib.auth.models import User
from django.urls import include, path
from oauth2_provider.contrib.rest_framework import (TokenHasReadWriteScope, TokenHasScope)
from rest_framework import generics, permissions, serializers
from api.models import Product
admin.autodiscover()

from oauth2_provider.decorators import protected_resource


# first we define the serializers
class ProdListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "itemno", "description", "price",)

class ProdDetailedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "itemno", "description", "description2", "price", "colour", "manufacturerCode")

# Create the API views

class Productlist(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = Product.objects.all()
    serializer_class = ProdListSerializer
    def get(self, request, *args, **kwargs):
        if not self.request.data == {}:    
            print(self.request.data)
            if not self.request.data['manufacturerCode'] == '':
                self.queryset = Product.objects.filter(manufacturerCode=self.request.data['manufacturerCode'])
        return super().get  (request, *args, **kwargs)

class ProductDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = Product.objects.all()
    serializer_class = ProdDetailedSerializer

# Setup the URLs and include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('Productlist/', Productlist.as_view()),
    path('Productlist/<pk>/', ProductDetail.as_view())
]