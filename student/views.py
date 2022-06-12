from django.shortcuts import render, redirect, reverse
from student.forms import StudentsignupForm
from student.models import Student
from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate, logout
from django.contrib.auth.models import User, auth #Imported User from Django

User = get_user_model()

# Create your views here.
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
                return redirect("/studentsignup")
            elif User.objects.filter(email=student_email).exists():
                messages.info(request, 'Email already used!')
                return redirect("/studentsignup")
            else:
                form = User.objects.create_user(username=Username, email=student_email, password=password)
                form.save()
                return redirect("/studentlogin")
        else:
            messages.info(request, 'Passwords do not match')
            return redirect("/studentsignup")
    else:
        form = StudentsignupForm
    return render(request, 'studentsignup.html', {'form': form})

        # username = request.POST['username']
        # first_name = request.POST['first_name']
        # last_name = request.POST['last_name']
        # email = request.POST['email']
        # password1 = request.POST['password1']
        # password2 = request.POST['password2']

        # if form:password == password2:
        #     if User.objects.filter(username=username).exists():
        #         messages.info(request, 'Username already exists!')
        #         return redirect('/studentsignup')

        #     elif User.objects.filter(email=email).exists():
        #         messages.info(request, 'This email has already being used!')
        #         return redirect('/studentsignup')

        #     else:
        #         user = User.objects.create_user(username=username, email=email, password=password1,
        #                                             first_name=first_name, last_name=last_name)
        #         user.save()
        #         return redirect('/studentlogin')

        # else:
        #     messages.info(request, "Passwords do not match")
        #     return redirect('/studentsignup')
    # else:
    #     return render(request, "studentsignup.html")

def studentlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/homepage')
        else:
            messages.info(request, 'Invalid Username or Password!')
            return redirect('/studentlogin')
    else:
        return render(request, 'studentlogin.html', {})


