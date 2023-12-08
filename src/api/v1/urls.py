from django.urls import path

from api.v1.carsharing import views as api_views

urlpatterns = [
    path("v1/health", api_views.health_check, name="health"),
    path("v1/cars", api_views.CarSharingView.as_view(), name="cars"),
    path("v1/offers", api_views.OfferView.as_view(), name="offers")
]
