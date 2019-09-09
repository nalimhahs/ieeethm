from django.urls import path, include
# from .views import ListAllEventsView, ListEventByCatagoryView, GetEventView, ListAllCatagoriesView
from .views import *
# urlpatterns = [
#     path('all', ListAllEventsView.as_view()),
#     path('catagory', ListEventByCatagoryView.as_view()),
#     path('event', GetEventView.as_view()),
#     path('all-catagories', ListAllCatagoriesView.as_view()),
# ]

urlpatterns = [
    path('', allCatagories),
    path('<slug:catagory>', catagoryListing),
    path('<slug:catagory>/<int:event_id>', eventListing),
]
