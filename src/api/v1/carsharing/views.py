import json

from django.http import HttpResponse
from django.views import View
from rest_framework import status

from apps.carsharing.views import CarService, OfferService, ServiceError
from apps.carsharing.helpers import ValidationError


def health_check(request):
    return HttpResponse("OK")


class CarSharingView(View):
    def __init__(self):
        self.car_service = CarService()

    def get(self, request):
        car_list = self.car_service.get_all_cars()
        return HttpResponse(
            json.dumps(car_list),
            content_type="application/json"
        )

    def post(self, request):
        json_data = request.body.decode("utf-8")
        data = json.loads(json_data)

        try:
            response_data = self.car_service.create_car(data)
            return HttpResponse(
                json.dumps(response_data),
                status=status.HTTP_201_CREATED,
                content_type="application/json",
            )
        except ServiceError as err:
            error_data = err.get_error_msg()
            return HttpResponse(
                json.dumps(error_data),
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content_type="application/json",
            )
        except ValidationError as err:
            error_data = err.get_error_msg()
            return HttpResponse(
                json.dumps(error_data),
                status=status.HTTP_400_BAD_REQUEST,
                content_type="application/json"
            )


class OfferView(View):
    def __init__(self):
        self.offer_service = OfferService()

    def get(self, request):
        offer_list = self.offer_service.get_all_offers()
        return HttpResponse(
            json.dumps(offer_list),
            status=status.HTTP_200_OK,
            content_type="application/json"
        )

    def post(self, request):
        json_data = request.body.decode("utf-8")
        data = json.loads(json_data)

        try:
            response_data = self.offer_service.create_offer(data=data)
            return HttpResponse(
                json.dumps(response_data),
                status=status.HTTP_201_CREATED,
                content_type="application/json"
            )
        except ServiceError as err:
            error_data = err.get_error_msg()
            return HttpResponse(
                json.dumps(error_data),
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content_type="application/json"
            )
        except ValidationError as err:
            error_data = err.get_error_msg()
            return HttpResponse(
                json.dumps(error_data),
                status=status.HTTP_400_BAD_REQUEST,
                content_type="application/json"
            )

    def delete(self, request):
        json_data = request.body.decode("utf-8")
        data = json.loads(json_data)
        offer_id = data.get('offer_id')

        try:
            self.offer_service.delete_offer(offer_id=offer_id)
            return HttpResponse(status=status.HTTP_204_NO_CONTENT)
        except ServiceError as err:
            error_data = err.get_error_msg()
            return HttpResponse(
                json.dumps(error_data),
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content_type="application/json"
            )
        except ValidationError as err:
            error_data = err.get_error_msg()
            return HttpResponse(
                json.dumps(error_data),
                status=status.HTTP_400_BAD_REQUEST,
                content_type="application/json"
            )

