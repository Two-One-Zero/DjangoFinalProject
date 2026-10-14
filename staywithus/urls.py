

from django.contrib import admin
from django.urls import path
from hotels import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('hotels/', views.hotels, name='hotels'),
    path('bookings/', views.bookings, name='bookings'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
]