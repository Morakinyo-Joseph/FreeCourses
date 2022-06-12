from django.shortcuts import render, redirect, reverse
from .models import Course, Lecturer
from .forms import CourseForm
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


User = get_user_model()


def course_list(request):
    course = Course.objects.all()
    return render(request, 'lecturer/course_list.html', {"course": course})



def course_create(request):
    form = CourseForm()
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teach:course-list')

    return render(request, "lecturer/course_creation.html", {"form": form})


def course_detail(request, pk):
    course = Course.objects.get(id=pk)
    return render(request, 'lecturer/course_detail.html', {"course": course})


def course_update(request, pk):
    course = Course.objects.get(id=pk)
    form = CourseForm(instance=course)
    if request.method == "POST":
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('teach:course-list')

    return render(request, 'lecturer/course_update.html', {"course": course,
                                                           "form": form})


def course_delete(request, pk):
    course = Course.objects.get(id=pk)
    course.delete()
    return redirect("teach:course-list")

def landing_page(request):
    if User.is_authenticated:
        return redirect('homepage')
    else:
        return render(request, "landing_page.html")


def homepage(request):
    return render(request, "homepage.html")


def register(request):
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
                return redirect('teach:signup')

            elif User.objects.filter(email=email).exists():
                messages.info(request, 'This email has already being used!')
                return redirect('teach:signup')

            else:
                new_user = User.objects.create_user(username=username, email=email, password=password1,
                                                    first_name=first_name, last_name=last_name)
                new_user.save()
                return redirect('teach:login')

        else:
            messages.info(request, "Passwords do not match")
            return redirect('teach:signup')

    else:
        return render(request, "register/signup.html")


def logging_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('teach:course-list')
        else:
            messages.info(request, 'Invalid Username or Password!')
            return redirect('teach:login')
    else:
        return render(request, "register/login.html")


def logging_out(request):
    pass    