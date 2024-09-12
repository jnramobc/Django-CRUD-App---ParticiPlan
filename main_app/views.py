# main_app/views.py

from django.shortcuts import render

from django.shortcuts import redirect, get_object_or_404

from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

# Import HttpResponse to send text-based responses
from django.http import HttpResponse

from .models import Event

from .models import Volunteer

from .models import Participation


from .forms import ParticipationForm

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


def volunteer_index(request):
    volunteers = Volunteer.objects.all()
    return render(request, 'volunteers/index.html', {'volunteers': volunteers})

def add_participation(request, event_id):
    # Find the event the participation is being added to
    event = Event.objects.get(id=event_id)

    # Create a form instance using POST data
    if request.method == 'POST':
        form = ParticipationForm(request.POST)

        # Check if the form is valid
        if form.is_valid():
            # Create a participation instance but don't save it yet
            new_participation = form.save(commit=False)
            # Assign the event to the participation
            new_participation.event = event
            # Save the participation to the database
            new_participation.save()
            
            # Redirect to the event detail page after submission
            return redirect('event-detail', pk=event_id)

    # If the form is not valid, redirect back to the event detail page
    return redirect('event-detail', pk=event_id)

def delete_participation(request, participation_id):
    # Get the participation object or return a 404 if not found
    participation = get_object_or_404(Participation, id=participation_id)
    
    # Store the related event ID for redirection later
    event_id = participation.event.id
    
    # Delete the participation object
    participation.delete()
    
    # Redirect back to the event detail page
    return redirect('event-detail', pk=event_id)

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

# Event Detail View with Participation Form
class EventDetail(DetailView):
    model = Event
    template_name = 'events/detail.html'

    # Override get_context_data to pass the form to the template
    def get_context_data(self, **kwargs):
        # Get the default context from the superclass
        context = super().get_context_data(**kwargs)
        
        # Add the ParticipationForm to the context
        context['participation_form'] = ParticipationForm()

        return context

# Event Create View
class EventCreate(CreateView):
    model = Event
    fields = '__all__'  
    template_name = 'events/event_form.html'  
    success_url = '/events/'  

# Event Update View
class EventUpdate(UpdateView):
    model = Event
    fields = '__all__'
    template_name = 'events/event_form.html'  
    success_url = '/events/'  

# Event Delete View
class EventDelete(DeleteView):
    model = Event
    template_name = 'events/event_confirm_delete.html'  # Confirm delete template
    success_url = '/events/'  
