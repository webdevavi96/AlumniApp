from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.hashers import make_password
from datetime import datetime
from .models import Blog, Event
from .models import Alumni, Teacher, Student as UserType

blogData = Blog.objects.all()
eventData = Event.objects.all()

# Create your views here.


def home(request):
    return render(request, 'index.html')


@login_required
def blogs(request):
    return render(request, 'pages/blogs.html', {"blogData": blogData})

@login_required
def events(request):
    current_datetime = datetime.now()
    for event in eventData:
        event_datetime = datetime.combine(event.date, event.time)
        if event_datetime > current_datetime:
            event.status = "Upcoming"
        elif event_datetime == current_datetime:
            event.status = "Ongoing"
        else:
            event.status = "Ended"

    return render(request, 'pages/events.html', {'eventData': eventData})

@login_required
def profile(request):
    return render(request, 'pages/profile.html')

def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = None
        if Alumni.objects.filter(email=email).exists():
            user = Alumni.objects.get(email=email)
        elif Teacher.objects.filter(email=email).exists():
            user = Teacher.objects.get(email=email)
        elif UserType.objects.filter(email=email).exists():
            user = UserType.objects.get(email=email)

        if user and user.password == make_password(password):
            request.session['user_id'] = user.id
            request.session['user_type'] = user.user_type
            return redirect("profile") 
        else:
            return HttpResponse("Invalid email or password.")

    return render(request, "pages/signIn.html")

def signUp(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        user_type = request.POST.get("user_type")
        branch = request.POST.get("branch")
        userPassword = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if userPassword != confirm_password:
            return HttpResponse("Password did not match.")
        else:
            if user_type == "alumni":
                Alumni.objects.create(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    phone=phone,
                    user_type=user_type,
                    password=make_password(userPassword),
                )
            elif user_type == "teacher":
                Teacher.objects.create(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    phone=phone,
                    user_type=user_type,
                    password=make_password(userPassword),
                )
            else:
                if not branch:
                    return HttpResponse("Please select your Branch.")
                UserType.objects.create(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    phone=phone,
                    branch=branch,
                    user_type=user_type,
                    password=make_password(userPassword),
                )

        return redirect("login")

    return render(request, "pages/signUp.html")


def logout(request):
    request.session.flush()
    return redirect("login")