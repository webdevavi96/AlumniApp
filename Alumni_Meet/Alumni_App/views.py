from django.shortcuts import render
from django.contrib.auth.decorators import login_required



# Create your views here.


def home(request):
    return render(request, 'index.html')


def blogs(request):
    return render(request, 'pages/blogs.html')

@login_required
def events(request):
    return render(request, 'pages/events.html')

@login_required
def profile(request):
    return render(request, 'pages/profile.html')

def login(request):
    return render(request, 'pages/signIn.html')

def signUp(request):
    
    return render(request, 'pages/signUp.html')