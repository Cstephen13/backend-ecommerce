from rest_framework import serializers

from offers.models import Offer


class OfferSerializer(serializers.ModelSerializer):

    class Meta:
        model = Offer
        fields = ('id', 'banner', 'init_offer', 'end_offer')
