from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.response import Response

from invoices.api.serializers import InvoiceSerializer
from invoices.models import Invoice, InvoiceProduct


class InvoiceApiViewSet(viewsets.ModelViewSet):
    serializer_class = InvoiceSerializer
    queryset = Invoice.objects.all()

    def create(self, request, *args, **kwargs):
        user = User.objects.get(username='carlos')
        data = request.data
        invoice = Invoice.objects.create(total_sale=data['total_sale'], payment=data['payment'], user_id=user.pk)
        invoice.save()
        products = data['products']
        for product in products:
            invoice_product = InvoiceProduct.objects.create(product_id=product['id'],
                                                            invoice_id=invoice.pk,
                                                            price_product=product['price_product'],
                                                            quantity=product['quantity'])
            invoice_product.save()

        serializer = InvoiceSerializer(invoice)
        return Response(serializer.data)

