# main_app/views.py

from django.shortcuts import render

# Import HttpResponse to send text-based responses
from django.http import HttpResponse

from .models import Event

from .models import Volunteer

# Define the home view function
def home(request):
    # Send a simple HTML response
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


def event_index(request):
    events = Event.objects.all() 
    return render(request, 'events/index.html', {'events': events})



def volunteer_index(request):
    volunteers = Volunteer.objects.all()
    return render(request, 'volunteers/index.html', {'volunteers': volunteers})

def event_detail(request, event_id):
    event = Event.objects.get(id=event_id)  
    return render(request, 'events/detail.html', {'event': event})


def volunteer_detail(request, volunteer_id):
    volunteer = Volunteer.objects.get(id=volunteer_id)
    return render(request, 'volunteers/detail.html', {'volunteer': volunteer})