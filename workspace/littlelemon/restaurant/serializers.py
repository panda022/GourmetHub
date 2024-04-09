# serializers.py in the restaurant app directory
from rest_framework import serializers
from .models import Menu
from .models import Booking 

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['ID', 'Title', 'Price', 'Inventory']  # Specify the fields to include


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking  # Specify the model to be serialized
        fields = '__all__'  # Serialize all fields of the Booking model