from rest_framework import serializers
from invoices.models import Invoice, InvoiceProduct


class InvoiceProductSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField()

    class Meta:
        model = InvoiceProduct
        fields = ('id', 'quantity', 'product', 'price_product')


class InvoiceSerializer(serializers.ModelSerializer):
    detail_products = InvoiceProductSerializer(many=True)
    user = serializers.StringRelatedField()

    class Meta:
        model = Invoice
        fields = ('id', 'user', 'number_invoice', 'total_sale', 'payment', 'payment_date', 'detail_products')
