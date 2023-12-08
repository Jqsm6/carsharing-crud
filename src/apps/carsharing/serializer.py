from rest_framework import serializers

from .models import Car, Offer, CarPydantic, OfferPydantic


class PydanticModelSerializer(serializers.ModelSerializer):
    def from_orm(self, instance):
        pydantic_model = self.Meta.model_pydantic.from_orm(instance)
        return pydantic_model

    class Meta:
        abstract = True


class CarSerializer(PydanticModelSerializer):
    class Meta:
        model = Car
        fields = ("car_brand", "car_model", "car_year", "status")
        pydantic_model = CarPydantic


class OfferSerializer(PydanticModelSerializer):
    class Meta:
        model = Offer
        fields = ("car_id", "renter_id")
        pydantic_model = OfferPydantic
