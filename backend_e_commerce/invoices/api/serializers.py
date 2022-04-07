from rest_framework import serializers
from invoices.models import Invoice
from products.api.serializers import ProductSerializer


class InvoiceSerializer(serializers.ModelSerializer):
    products = ProductSerializer(read_only=True, many=True)

    class Meta:
        model = Invoice
        fields = ('id', 'user', 'number_invoice', 'total_sale', 'payment', 'payment_date', 'products')
