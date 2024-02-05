from .models import *
from rest_framework import serializers

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'

class PassangerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'

class ReservationSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'