from django.shortcuts import render
import datetime  # Import the datetime module

# Create your views here.
from django.http import HttpResponse

# def sayHello(request):
#     return HttpResponse('Hello World')
def index(request):
    current_year = datetime.datetime.now().year  # Get the current year
    return render(request, 'index.html', {'current_year': current_year})