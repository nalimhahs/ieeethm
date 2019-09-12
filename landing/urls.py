from django.urls import include, path

from .views import landingPage, aboutPage, contactPage

urlpatterns = [
  path('about', aboutPage),
  path('contact', contactPage)
]