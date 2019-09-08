from django.contrib import admin
from .models import Event, Catagory, Organizer

# Register your models here.

admin.site.register(Event)
admin.site.register(Catagory)
admin.site.register(Organizer)