from rest_framework import viewsets
from offers.api.serializers import OfferSerializer
from offers.models import Offer


class OfferApiViewSet(viewsets.ModelViewSet):
    serializer_class = OfferSerializer
    queryset = Offer.objects.all()
