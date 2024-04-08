from django.contrib import admin
from .models import Menu, Booking  # Import the models from the models.py file in the same directory

# Register your models here.
admin.site.register(Menu)
admin.site.register(Booking)