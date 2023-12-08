from django.contrib import admin

from .models import Car, Offer


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("car_brand", "car_model", "car_year", "status")
    list_filter = ("status",)
    search_fields = ("car_brand", "car_model", "car_year")


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ("offer_id", "car_id", "renter_id")
