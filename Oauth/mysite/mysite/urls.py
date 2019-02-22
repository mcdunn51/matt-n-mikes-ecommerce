from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
from rest_framework import generics, permissions, serializers
from django.urls import path, include
from django.contrib.auth.models import User, Group
from django.contrib import admin
from data.models import Product
admin.autodiscover()


# first we define the serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', "first_name", "last_name")


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ("name")

class ProdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "itemno", "description", "description2", "price", "colour", "manufacturerCode")

# Create the API views

class UserList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetails(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    required_scopes = ['groups']
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class Productlist(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = Product.objects.all()
    serializer_class = ProdSerializer


# Setup the URLs and include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('users/', UserList.as_view()),
    path('users/<pk>/', UserDetails.as_view()),
    path('groups/', GroupList.as_view()),
    path('Productlist/', Productlist.as_view())
]