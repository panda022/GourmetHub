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
            form.save()
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