

from django.shortcuts import render


def home(request):
    return render(request, 'hotels/home.html')


def hotels(request):
    return render(request, 'hotels/hotels.html')


def bookings(request):
    return render(request, 'hotels/bookings.html')


def contact(request):
    return render(request, 'hotels/contact.html')


def about(request):
    return render(request, 'hotels/about.html')
