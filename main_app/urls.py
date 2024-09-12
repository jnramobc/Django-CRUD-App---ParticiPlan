from django.urls import path
from . import views # Import views to connect routes to view functions

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('volunteers/', views.volunteer_index, name='volunteer-index'),
    path('volunteers/<int:volunteer_id>/', views.volunteer_detail, name='volunteer-detail'),
    path('events/', views.event_index, name='event-index'),
    path('events/<int:event_id>/', views.event_detail, name='event-detail'),
]
