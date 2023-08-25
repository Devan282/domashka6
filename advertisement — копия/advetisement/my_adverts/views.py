from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def topSellers(request):
    return render(request, 'top-sellers.html')

def Register(request):
    return render(request, 'register.html')

def Profile(request):
    return render(request, 'profile.html')

def Login(request):
    return render(request, 'login.html')

# Create your views here.
