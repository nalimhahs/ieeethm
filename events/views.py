from django.shortcuts import render
from django.http import Http404

from .models import Event, Catagory

# Create your views here.

def allCatagories(request):
  catagories = Catagory.objects.all()
  return render(request, 'events/index.html', { 'catagories': catagories })

def catagoryListing(request, catagory):
  events = Event.objects.filter(catagory__name=catagory)
  try:
    p = Catagory.objects.get(name=catagory)
  except Catagory.DoesNotExist:
    raise Http404
  return render(request, 'events/eventlist.html', { 'events': events, 'catagory': catagory })

def eventListing(request, catagory, event_id):
  event = Event.objects.filter(event_id=event_id)
  return render(request, 'events/singleevent.html', { 'event': event, 'eventName': event[0].name })
