from rest_framework import serializers
from invoices.models import Invoice, InvoiceProduct
from products.api.serializers import ProductSerializer


class InvoiceProductSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField()

    class Meta:
        model = InvoiceProduct
        fields = ('id', 'product', 'quantity', 'price_product')


class InvoiceSerializer(serializers.ModelSerializer):
    products = InvoiceProductSerializer(read_only=True, many=True, source='invoice_products')

    class Meta:
        model = Invoice
        fields = ('id', 'user', 'number_invoice', 'total_sale', 'payment', 'payment_date', 'products')
