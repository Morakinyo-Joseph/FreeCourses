from django.shortcuts import render, reverse, redirect
from django.views import generic
from .models import Course, Lecturer
from .forms import CourseForm
from django.contrib.auth import get_user_model
from django.contrib import messages
from datetime import datetime

User = get_user_model()


def landing_page(request):
    if User.is_authenticated:
        return redirect('homepage')
    else:
        return render(request, "landing_page.html")


def homepage(request):
    return render(request, "homepage.html")


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists!')
                return redirect('signup')

            elif User.objects.filter(email=email).exists():
                messages.info(request, 'This email has already being used!')
                return redirect('signup')

            else:
                new_user = User.objects.create_user(username=username, email=email, password=password1,
                                                    first_name=first_name, last_name=last_name)
                new_user.save()
                return redirect('login')

        else:
            messages.info(request, "Passwords do not match")
            return redirect('signup')

    else:
        return render(request, "registration/signup.html")


def course_list(request):
    course = Course.objects.all()
    return render(request, 'lecturer/course_list.html', {"course": course})


def course_creation(request):
    course = Course.objects.all()
    form = CourseForm()

    return render(request, "lecturer/course_creation.html", {"form": form})


def course_detail(request, pk):
    course = Course.objects.get(id=pk)
    return render(request, 'lecturer/course_detail.html', {"course": course})


def course_update(request, pk):
    course = Course.objects.get(id=pk)
    form_update = CourseForm(instance=course)

    if request.method == "POST":
        form_update = CourseForm(instance=course)
        if form_update.is_valid:
            form_update.save()
            return redirect("/teach")

    return render(request, 'lecturer/course_update.html', {"course": course,
                                                           "form": form_update})


def course_delete(request, pk):
    course = Course.objects.get(id=pk)
    course.delete()
    return redirect("/teach")








