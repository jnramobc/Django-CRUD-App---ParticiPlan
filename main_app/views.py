# main_app/views.py

from django.shortcuts import render

# Import HttpResponse to send text-based responses
from django.http import HttpResponse

# Define the home view function
def home(request):
    # Send a simple HTML response
    return HttpResponse('<h1>Welcome to ParticiPlan!</h1>')

def about(request):
    return render(request, 'about.html')

# views.py
# views.py

class Volunteer:
    def __init__(self, name, email, role, bio, years_of_experience, available):
        self.name = name
        self.email = email
        self.role = role
        self.bio = bio
        self.years_of_experience = years_of_experience
        self.available = available

# Create a list of Volunteer instances with mock data
volunteers = [
    Volunteer(
        name='Alice Johnson',
        email='alice.johnson@example.com',
        role='Event Coordinator',
        bio='Passionate about organizing impactful community events.',
        years_of_experience=5,
        available=True
    ),
    Volunteer(
        name='Bob Smith',
        email='bob.smith@example.com',
        role='Fundraiser',
        bio='Expert in organizing fundraising campaigns.',
        years_of_experience=3,
        available=False
    ),
    Volunteer(
        name='Carla Brown',
        email='carla.brown@example.com',
        role='Social Media Manager',
        bio='Loves creating engaging content for social platforms.',
        years_of_experience=2,
        available=True
    ),
    Volunteer(
        name='David Green',
        email='david.green@example.com',
        role='Logistics Specialist',
        bio='Ensures everything runs smoothly, from setup to teardown.',
        years_of_experience=4,
        available=True
    )
]

# views.py

def volunteer_index(request):
    # Render the volunteers/index.html template with the volunteers data
    return render(request, 'volunteers/index.html', {'volunteers': volunteers})

