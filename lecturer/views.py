from django.shortcuts import render, reverse, redirect
from django.views import generic
from .models import Course
from .forms import CourseForm
from django.contrib.auth import get_user_model
from django.contrib import messages

User = get_user_model()

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

    else:
        return render(request, "registration/signup.html")

# class SignupView(generic.CreateView):
#     template_name = "registration/signup.html"
#     form_class = CustomUserCreationForm
#
#     def get_success_url(self):
#         return reverse("login")


def course_list(request):
    course = Course.objects.all()
    return render(request, 'lecturer/course_list.html', {"course": course})

# class CourseListView(generic.ListView):
#     template_name = "lecturer/course_list.html"
#     queryset = Course.objects.all()
#     context_object_name = "course"


# def course_create(request):
#     course = Course.objects.all()
#     if request.method == "POST":
#         lecturer_name = request.POST['lecturer']
#         category = request.POST['category']
#         topic = request.POST['topic']
#         content = request.POST['content']
#
#         new_course = Course.objects.create(lecturer=lecturer_name, category=category, topic=topic, content=content)
#         new_course.save()
#         return render('lecturer:course-detail')
#     else:
#         return render(request, 'lecturer/course_creation.html', {"course": course})


class CourseCreateView(generic.CreateView):
    template_name = "lecturer/course_creation.html"
    queryset = Course.objects.all()
    form_class = CourseForm

    def get_success_url(self):
        return reverse("teach:course-list")


def course_detail(request, pk):
    course = Course.objects.get(id=pk)
    return render(request, 'lecturer/course_detail.html', {"course": course})


# class CourseDetailView(generic.DetailView):
#     template_name = "lecturer/course_detail.html"
#     queryset = Course.objects.all()
#     context_object_name = "course"



def course_update(request, pk):
    course = Course.objects.get(id=pk)
    return render(request, 'lecturer/course_update.html', {"course": course})


# class CourseUpdateView(generic.UpdateView):
#     template_name = "lecturer/course_update.html"
#     queryset = Course.objects.all()
#     form_class = CourseForm
#
#     def get_success_url(self):
#         return reverse("teach:course-list")
#


def course_delete(request):
    pass
#
# class CourseDeleteView(generic.DeleteView):
#     template_name = "lecturer/course_delete.html"
#     queryset = Course.objects.all()
#
#     def get_success_url(self):
#         return reverse("teach:course-list")







