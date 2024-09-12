from django.contrib import admin
from .models import Volunteer, Event, Participation

# Register your models here.
admin.site.register(Event)
admin.site.register(Volunteer)
admin.site.register(Participation)