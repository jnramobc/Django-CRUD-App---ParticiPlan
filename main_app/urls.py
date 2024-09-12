from django.urls import path
from . import views # Import views to connect routes to view functions

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('volunteers/', views.volunteer_index, name='volunteer-index'),
    path('events/', views.event_index, name='event-index'),
]
