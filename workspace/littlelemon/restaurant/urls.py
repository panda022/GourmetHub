#define URL route for index() view
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.index, name='home'),
    path('menu/', views.menu, name='menu'),
    path('about/', views.about, name='about'),
    path('booking/', views.book, name='book'),
    path('bookings/', views.bookings, name='bookings'),
]