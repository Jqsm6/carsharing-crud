from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Car, CarSerializer

class CarListCreateView(APIView):
    def get(self, request, format=None):
        car_list = Car.objects.all()
        serializer = CarSerializer(car_list, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
