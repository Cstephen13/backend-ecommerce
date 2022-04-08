from rest_framework import serializers

from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()

    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'description', 'image', 'category')
