from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib import messages


User = get_user_model()


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
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request, 'This email has already being used!')
                return redirect('register')

            else:
                new_user = User.objects.create_user(username=username, email=email, password=password1,
                                                    first_name=first_name, last_name=last_name)
                new_user.save()
                return redirect('login')

        else:
            messages.info(request, "Passwords do not match")
            return redirect('register')

    else:
        return render(request, "register/register.html")
