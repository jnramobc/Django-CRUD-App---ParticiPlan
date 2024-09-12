# main_app/views.py

from django.shortcuts import render

# Import HttpResponse to send text-based responses
from django.http import HttpResponse

from .models import Event

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
    # Render the volunteers/index.html template with the volunteers data
    return render(request, 'volunteers/index.html', {'volunteers': volunteers})

def event_detail(request, event_id):
    event = Event.objects.get(id=event_id)  # Fetch the specific event by ID
    return render(request, 'events/detail.html', {'event': event})
