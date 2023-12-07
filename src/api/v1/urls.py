from django.urls import path
from api.v1.carsharing import views as api_views
from apps.carsharing import views as app_views

urlpatterns = [
    path('v1/health', api_views.health_check, name="health"),
    path('v1/cars', app_views.CarListCreateView.as_view(), name="cars"),
]