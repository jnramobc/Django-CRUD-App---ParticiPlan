from django.urls import path
from . import views # Import views to connect routes to view functions
from .views import VolunteerCreate, VolunteerUpdate, VolunteerDelete, VolunteerDetail
from .views import EventDetail, EventCreate, EventUpdate, EventDelete
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('volunteers/', views.volunteer_index, name='volunteer-index'),
    path('volunteers/<int:pk>/', VolunteerDetail.as_view(), name='volunteer-detail'),
    path('volunteers/create/', VolunteerCreate.as_view(), name='volunteer-create'),
    path('volunteers/<int:pk>/update/', VolunteerUpdate.as_view(), name='volunteer-update'),
    path('volunteers/<int:pk>/delete/', VolunteerDelete.as_view(), name='volunteer-delete'),
    path('events/', views.event_index, name='event-index'),
    path('events/<int:pk>/', EventDetail.as_view(), name='event-detail'),
    path('events/create/', EventCreate.as_view(), name='event-create'),
    path('events/<int:pk>/update/', EventUpdate.as_view(), name='event-update'),
    path('events/<int:pk>/delete/', EventDelete.as_view(), name='event-delete'),
    path('events/<int:event_id>/add-participation/', views.add_participation, name='add-participation'),
    path('participation/<int:participation_id>/delete/', views.delete_participation, name='delete-participation'),
    path('accounts/signup/', views.signup, name='signup'),
    
]
