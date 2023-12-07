from api.v1.carsharing import views as api_views
from apps.carsharing import views as app_views
from django.urls import path

urlpatterns = [
    path("v1/health", api_views.health_check, name="health"),
    path("v1/cars", app_views.CarCrudView.as_view(), name="cars"),
    path("v1/offers", app_views.OfferCrudView.as_view(), name="offers"),
]
