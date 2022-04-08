from rest_framework import serializers

from categories.models import Category
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    category_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Category.objects.all(),
                                                     source='category')
    category = serializers.StringRelatedField()

    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'description', 'image', 'category', 'category_id')
