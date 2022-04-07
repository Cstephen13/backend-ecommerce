from rest_framework import viewsets

from categories.api.serializers import CategorySerializer
from categories.models import Category


class CategoryApiViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
