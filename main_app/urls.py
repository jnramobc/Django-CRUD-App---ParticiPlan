from django.urls import path
from . import views # Import views to connect routes to view functions
from .views import VolunteerCreate, VolunteerUpdate, VolunteerDelete, VolunteerDetail


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('volunteers/', views.volunteer_index, name='volunteer-index'),
    path('volunteers/<int:pk>/', VolunteerDetail.as_view(), name='volunteer-detail'),
    path('volunteers/create/', VolunteerCreate.as_view(), name='volunteer-create'),
    path('volunteers/<int:pk>/update/', VolunteerUpdate.as_view(), name='volunteer-update'),
    path('volunteers/<int:pk>/delete/', VolunteerDelete.as_view(), name='volunteer-delete'),
    path('events/', views.event_index, name='event-index'),
    path('events/<int:event_id>/', views.event_detail, name='event-detail'),
]
