from .models import Car


class ValidationError(Exception):
    def __init__(self, msg):
        self.msg = "ValidationError: " + msg
        self.err_msg = msg

    def get_error_msg(self):
        return self.msg


def validation_offer(data):
    car_id = data.get('car_id')

    try:
        car = Car.objects.get(car_id=car_id)
        if car.status == "BSY":
            raise ValidationError("the car is busy")
    except Car.DoesNotExist:
        raise ValidationError("сar does not exist")

    return car
