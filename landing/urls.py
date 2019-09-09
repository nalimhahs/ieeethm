from django.urls import include, path

from .views import landingPage, aboutPage, contactPage

urlpatterns = [
  path('', landingPage),
  path('about', aboutPage),
  path('contact', contactPage)
]