"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.contrib.auth.models import User
from django.urls import include, path
from oauth2_provider.contrib.rest_framework import (TokenHasReadWriteScope, TokenHasScope)
from rest_framework import generics, permissions, serializers
from api.models import Product
admin.autodiscover()

# first we define the serializers
class ProdSerializer(serializers.ModelSerializer):
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
    serializer_class = ProdSerializer

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
