from rest_framework import viewsets
from .models import Booking  # Import the Booking model
from .serializers import BookingSerializer  # Import the BookingSerializer

from django.shortcuts import render
import datetime  # Import the datetime module

from django.core import serializers
import json
from .forms import BookingForm


# Create your views here.
from django.http import HttpResponse

import requests
import json


# def sayHello(request):
#     return HttpResponse('Hello World')
def index(request):
    current_year = datetime.datetime.now().year  # Get the current year
    return render(request, 'index.html', {'current_year': current_year})


def menu(request):
    return render(request, 'menu.html')

def about(request):
    return render(request, 'about.html')


# def booking(request):
#     return render(request, 'book.html')


def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            # Save the booking to the database
            new_booking = form.save()


            # Prepare data for sending to API Gateway
            data = {
                'ID': new_booking.ID,
                'Name': new_booking.Name,
                'No_of_guests': new_booking.No_of_guests,
                'BookingDate': new_booking.BookingDate.strftime('%Y-%m-%d %H:%M')
            }

            # URL of my API Gateway endpoint
            # api_gateway_url = 'https://qffzlcdrfh.execute-api.us-east-1.amazonaws.com/term-api-test/user'
            api_gateway_url = 'https://o0gf3wqtv5.execute-api.us-east-1.amazonaws.com/test-sns/user'
            # Sending a POST request to the API Gateway
            try:
                response = requests.post(api_gateway_url, json=data)
                response.raise_for_status()
                # Optional: Do something with the response
            except requests.exceptions.RequestException as e:
                # Handle any errors here (e.g., log them)
                print(e)

    context = {'form':form}
    return render(request, 'book.html', context)

def bookings(request):
    date = request.GET.get('date', datetime.date.today())
    bookings = Booking.objects.all()
    booking_json = serializers.serialize('json', bookings)
    return render(request, 'bookings.html', {'bookings': booking_json})







class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()  # Fetch all Booking objects
    serializer_class = BookingSerializer  # Use BookingSerializer to serialize data