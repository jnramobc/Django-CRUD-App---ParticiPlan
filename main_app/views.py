# main_app/views.py

from django.shortcuts import render

from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

# Import HttpResponse to send text-based responses
from django.http import HttpResponse

from .models import Event

from .models import Volunteer

from django.urls import reverse_lazy


# Define the home view function
def home(request):
    # Send a simple HTML response
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


def event_index(request):
    events = Event.objects.all() 
    return render(request, 'events/index.html', {'events': events})

def event_detail(request, event_id):
    event = Event.objects.get(id=event_id)  
    return render(request, 'events/detail.html', {'event': event})

def volunteer_index(request):
    volunteers = Volunteer.objects.all()
    return render(request, 'volunteers/index.html', {'volunteers': volunteers})


from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from .models import Volunteer
from django.urls import reverse_lazy

# Volunteer Create View
class VolunteerCreate(CreateView):
    model = Volunteer
    fields = ['name', 'email', 'phone_number', 'availability']
    template_name = 'volunteers/volunteer_form.html'
    success_url = reverse_lazy('volunteer-index')

# Volunteer Detail View
class VolunteerDetail(DetailView):
    model = Volunteer
    template_name = 'volunteers/detail.html'

# Volunteer Update View
class VolunteerUpdate(UpdateView):
    model = Volunteer
    fields = ['name', 'email', 'phone_number', 'availability']
    template_name = 'volunteers/volunteer_form.html'
    success_url = reverse_lazy('volunteer-index')

# Volunteer Delete View
class VolunteerDelete(DeleteView):
    model = Volunteer
    template_name = 'volunteers/volunteer_confirm_delete.html'
    success_url = reverse_lazy('volunteer-index')
