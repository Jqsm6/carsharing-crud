from django.urls import path
from api.v1.carsharing import views

urlpatterns = [
    path('v1/health', views.health_check, name="health")
]