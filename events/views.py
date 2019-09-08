from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from .models import Event, Catagory
from .serializers import EventSerializer, CatagorySerializer

# Create your views here.

class ListAllEventsView(generics.ListAPIView):

    queryset = Event.objects.all()
    serializer_class = EventSerializer


class ListAllCatagoriesView(generics.ListAPIView):

    queryset = Catagory.objects.all()
    serializer_class = CatagorySerializer


class ListEventByCatagoryView(generics.ListAPIView):

    serializer_class = EventSerializer

    def get_queryset(self):
        try:
            catagory = self.request.query_params.get('catagory')
        except:
            return Response({ "error": "Invalid Parameters" })
        return Event.objects.filter(catagory__name=catagory)


class GetEventView(generics.ListAPIView):

    serializer_class = EventSerializer

    def get_queryset(self):
        try:
            event_id = self.request.query_params.get('event')
        except:
            return Response({ "error": "Invalid Parameters" })
        return Event.objects.filter(event_id=event_id)