from django.urls import path, include
from .views import ListAllEventsView, ListEventByCatagoryView, GetEventView, ListAllCatagoriesView

urlpatterns = [
    path('all', ListAllEventsView.as_view()),
    path('catagory', ListEventByCatagoryView.as_view()),
    path('event', GetEventView.as_view()),
    path('all-catagories', ListAllCatagoriesView.as_view()),
]
