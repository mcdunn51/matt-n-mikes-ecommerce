from rest_framework import generics, permissions
from oauth2_provider.contrib.rest_framework import (TokenHasReadWriteScope, TokenHasScope)
from api.models import Product
from api.serializers import ProdListSerializer, ManufacturerSerializer

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
    queryset = Product.objects.values('manufacturerCode').distinct()
    serializer_class = ManufacturerSerializer