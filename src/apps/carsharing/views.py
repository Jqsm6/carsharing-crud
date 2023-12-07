import json

from django.http import HttpResponse
from django.views import View
from rest_framework import status

from .models import Car, Offer
from .serializer import CarSerializer, OfferSerializer


class CarIsBusy(Exception):
    pass


class CarCrudView(View):
    def post(self, request, format=None):
        json_data = request.body.decode("utf-8")
        data = json.loads(json_data)
        serializer = CarSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            response_data = serializer.data
            json_response = json.dumps(response_data)
            return HttpResponse(
                json_response,
                status=status.HTTP_201_CREATED,
                content_type="application/json",
            )

        error_data = serializer.errors
        json_error = json.dumps(error_data)
        return HttpResponse(
            json_error,
            status=status.HTTP_400_BAD_REQUEST,
            content_type="application/json",
        )

    def get(self, request, format=None):
        car_list = Car.objects.all()
        serializer = CarSerializer(car_list, many=True)
        data = serializer.data
        json_data = json.dumps(data)
        return HttpResponse(json_data, content_type="application/json")


class OfferCrudView(View):
    def post(self, request, format=None):
        json_data = request.body.decode("utf-8")
        data = json.loads(json_data)
        serializer = OfferSerializer(data=data)

        if serializer.is_valid():
            serializer.save()

            car_id = data.get("car_id")
            try:
                car = Car.objects.get(car_id=car_id)
                if car.status == "BSY":
                    raise CarIsBusy
                car.status = "BSY"
                car.save()
            except Car.DoesNotExist:
                print("Car does not exist.")
                return HttpResponse(status=status.HTTP_404_NOT_FOUND)
            except CarIsBusy:
                print("Car is busy.")
                return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

            response_data = serializer.data
            json_response = json.dumps(response_data)
            return HttpResponse(
                json_response,
                status=status.HTTP_201_CREATED,
                content_type="application/json",
            )

        error_data = serializer.errors
        json_error = json.dumps(error_data)
        return HttpResponse(
            json_error,
            status=status.HTTP_400_BAD_REQUEST,
            content_type="application/json",
        )

    def get(self, request, format=None):
        offer_list = Offer.objects.all()
        serializer = OfferSerializer(offer_list, many=True)
        data = serializer.data
        json_data = json.dumps(data)
        return HttpResponse(json_data, content_type="application/json")

    def delete(self, request, format=None):
        json_data = request.body.decode("utf-8")
        data = json.loads(json_data)
        offer_id = data.get("offer_id")

        try:
            offer = Offer.objects.get(offer_id=offer_id)

            car = offer.car_id
            car.status = "RDY"
            car.save()

            offer.delete()
            return HttpResponse(status=status.HTTP_204_NO_CONTENT)

        except Offer.DoesNotExist:
            return HttpResponse("Offer not found.", status=status.HTTP_404_NOT_FOUND)
