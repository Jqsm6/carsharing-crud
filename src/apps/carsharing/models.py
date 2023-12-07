from django.contrib.auth import get_user_model
from django.db import models
from rest_framework import serializers


class Car(models.Model):
    """Rental car model."""

    car_id = models.AutoField(primary_key=True)
    car_brand = models.CharField("Car brand", max_length=50)
    car_model = models.CharField("Car model", max_length=50)
    car_year = models.CharField("Car year", max_length=4)

    STATUS_CHOICES = [("RDY", "Ready"), ("BSY", "Busy")]
    status = models.CharField(
        "Status", max_length=5, choices=STATUS_CHOICES, default="RDY"
    )

    def __str__(self):
        return f"{self.car_brand} - {self.car_model} - {self.car_year} - {self.status}"


class Offer(models.Model):
    """Offer model."""

    offer_id = models.AutoField(primary_key=True)
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE)
    renter = models.ForeignKey(
        get_user_model(), on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return f"{self.car_id} - {self.renter}"


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ("car_brand", "car_model", "car_year", "status")


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = ("car_id", "renter", "offer_id")
