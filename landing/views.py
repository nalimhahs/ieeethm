from django.shortcuts import render

# Create your views here.

def landingPage(request):
  return render(request, 'landing/landingpage.html', {})

def aboutPage(request):
  return render(request, 'landing/about.html', {})

def contactPage(request):
  return render(request, 'landing/contact.html', {})