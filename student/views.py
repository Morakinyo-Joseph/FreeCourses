from django.shortcuts import render, redirect
from student.forms import StudentloginForm, StudentsignupForm
from student.models import Student
from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate, logout, login
from django.contrib.auth import get_user_model
from lecturer.models import Course


User = get_user_model()



def course_view(request):
    courses = Course.objects.all()
    return render(request, "student/course_view.html", {"course": courses})


def studentsignup(request):
    form = StudentsignupForm

    if request.method == 'POST':
        form = StudentsignupForm(request.POST)
        Username = request.POST['Username']
        student_email = request.POST['student_email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            
            if User.objects.filter(username=Username).exists():
                messages.info(request, 'Username already exists!')
                return redirect("learn:signup")

            elif User.objects.filter(email=student_email).exists():
                messages.info(request, 'Email already used!')
                return redirect("learn:signup")

            else:
                form = User.objects.create_user(username=Username, email=student_email, password=password)
                form.save()
                return redirect("learn:login")
        else:
            messages.info(request, 'Passwords do not match')
            return redirect("learn:signup")
    else:
        form = StudentsignupForm
    return render(request, 'student_register/studentsignup.html', {'form': form})


def studentlogin(request): #Added model form to this view, let's hope it works:)
    form = StudentloginForm

    if request.method == 'POST':
        form = StudentloginForm(request.POST)
        Username = request.POST['Username']
        password = request.POST['password']

        user = authenticate(username=Username, password=password)

        if user is not None:
            login(request, user)
            return redirect('learn:course-view')
        else:
            messages.info(request, 'Invalid Username or Password!')
            return redirect('learn:login')
    else:
        return render(request, 'student_register/studentlogin.html', {'form': form})


def studentlogout(request):
    pass