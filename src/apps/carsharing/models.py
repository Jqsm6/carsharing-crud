from django.db import models


class Car(models.Model):
    """Rental car model."""

    car_brand = models.CharField('Car brand', max_length=50)
    car_model = models.CharField('Car model', max_length=50)
    car_year = models.CharField('Car year', max_length=4)
    status = models.CharField('Status', max_length=10, choices=[('Ready', 'Busy')])

    def __str__(self):
        return f"{self.car_brand} - {self.car_model}"

