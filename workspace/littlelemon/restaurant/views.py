from rest_framework import viewsets
from .models import Booking  # Import the Booking model
from .serializers import BookingSerializer  # Import the BookingSerializer

from django.shortcuts import render
import datetime  # Import the datetime module


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


def booking(request):
    return render(request, 'book.html')


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()  # Fetch all Booking objects
    serializer_class = BookingSerializer  # Use BookingSerializer to serialize data