from django.contrib import admin
from .models import Event
from .models import Volunteer

# Register your models here.
admin.site.register(Event)
admin.site.register(Volunteer)