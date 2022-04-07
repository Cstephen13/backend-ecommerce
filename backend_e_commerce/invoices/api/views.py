from rest_framework import viewsets

from invoices.api.serializers import InvoiceSerializer
from invoices.models import Invoice


class InvoiceApiViewSet(viewsets.ModelViewSet):
    serializer_class = InvoiceSerializer
    queryset = Invoice.objects.all()
