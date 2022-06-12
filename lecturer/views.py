from django.shortcuts import render, redirect, reverse
from .models import Course, Lecturer
from .forms import CourseForm
from django.contrib import messages
<<<<<<< HEAD

User = get_user_model()  #This isn't needed since User is imported directly

# I changed from the generic class views to functions
# the class views were left commented


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
            return redirect('login')

    else:
        return render(request, "registration/signup.html")

# class SignupView(generic.CreateView):
#     template_name = "registration/signup.html"
#     form_class = CustomUserCreationForm
#
#     def get_success_url(self):
#         return reverse("login")
=======
from django.views import generic
>>>>>>> c97dd558a16ad29d17ae430f3e3d253d017f9629


def course_list(request):
    course = Course.objects.all()
    return render(request, 'lecturer/course_list.html', {"course": course})


# class CourseCreateView(generic.CreateView):
#     template_name = "lecturer/course_creation.html"
#     queryset = Course.objects.all()
#     form_class = CourseForm
#
#     def get_success_url(self):
#         return reverse("teach:course-list")
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
    return redirect("/teach")








