from rest_framework import serializers

from .models import Car, Offer


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ("car_brand", "car_model", "car_year", "status")


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = ("car_id", "renter_id")
