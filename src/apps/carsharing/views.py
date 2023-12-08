import logging

from .serializer import CarSerializer, OfferSerializer
from .models import Car, Offer
from .helpers import validation_offer, ValidationError


class ServiceError(Exception):
    def __init__(self, msg):
        self.msg = msg
        self.error_msg = f"ServiceError: {msg}"

    def get_error_msg(self):
        return self.error_msg


class CarService:
    def create_car(self, data):
        serializer = CarSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        else:
            raise ServiceError(serializer.errors)

    def get_all_cars(self):
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return serializer.data


class OfferService:
    def create_offer(self, data):
        serializer = OfferSerializer(data=data)
        if serializer.is_valid():
            serializer.save()

            try:
                car = validation_offer(serializer.data)
                car.status = "BSY"
                car.save()
                return serializer.data
            except ValidationError as err:
                logging.error(err.get_error_msg())
                raise err

        error_data = serializer.errors
        print(error_data)
        if 'car_id' or 'renter_id' in error_data:
            error_message = "does_not_exist"
            raise ValidationError(error_message)
        raise ServiceError(error_data)

    def get_all_offers(self):
        offers = Offer.objects.all()
        serializer = OfferSerializer(offers, many=True)
        return serializer.data

    def delete_offer(self, offer_id):
        try:
            offer = Offer.objects.get(offer_id=offer_id)
            car = offer.car_id
            car.status = "RDY"
            car.save()
            offer.delete()
        except Offer.DoesNotExist:
            raise ValidationError("offer does not exist")
