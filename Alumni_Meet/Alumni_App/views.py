from django.shortcuts import render
from django.contrib.auth.decorators import login_required
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
    return render(request, 'pages/signIn.html')

def signUp(request):
    if request.method == "POST":
        # Get form data
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        user_type = request.POST.get("user_type")
        branch = request.POST.get("branch")  # For Student

        # Validate required fields
        if not first_name or not last_name or not email or not phone or not user_type:
            return render(request, "pages/signUp.html")

        # Save data based on user type
        if user_type == "alumni":
            if not graduation_year:
                messages.error(request, "Graduation year is required for Alumni.")
                return render(request, "pages/signUp.html")
            Alumni.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                user_type=user_type,
            )
            print(f"Alumni Created: {alumni}")

        elif user_type == "teacher":
            Teacher.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                user_type=user_type,
            )
            print(f"Teacher Created: {teacher}")

        else:
            if not branch:
                messages.error(request, "Branch is required for Students.")
                return render(request, "pages/signUp.html")
            UserType.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                branch=branch,
                user_type=user_type,
            )
            print(f"Student Created: {student}")
        return redirect("login")  # Redirect to login page after successful signup

    return render(request, "pages/signUp.html")