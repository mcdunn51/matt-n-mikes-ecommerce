from django.contrib import admin
from django.contrib.auth.models import User
from django.urls import include, path
from oauth2_provider.contrib.rest_framework import (TokenHasReadWriteScope, TokenHasScope)
from rest_framework import generics, permissions
from rest_framework.authtoken.views import obtain_auth_token
from .view import Productlist, Manufacturerlist, AddressList, ProdDetailed
admin.autodiscover()

# Setup the URLs and include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('Token/', obtain_auth_token, name='api_token_auth'),
    path('Productlist/', Productlist.as_view()),
    path('ProductDetailed/', ProdDetailed.as_view()),
    path('Manufacturer/', Manufacturerlist.as_view()),
    path('Address/', AddressList.as_view())
]