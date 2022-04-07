from rest_framework import viewsets

from products.api.serializers import ProductSerializer
from products.models import Product


class ProductsApiViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
