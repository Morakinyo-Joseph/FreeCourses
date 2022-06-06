from django.shortcuts import render, reverse
from django.views import generic
from .models import Course
from .forms import CourseForm, CustomUserCreationForm


class SignupView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse("login")


class CourseListView(generic.ListView):
    template_name = "lecturer/course_list.html"
    queryset = Course.objects.all()
    context_object_name = "course"


class CourseDetailView(generic.DetailView):
    template_name = "lecturer/course_detail.html"
    queryset = Course.objects.all()
    context_object_name = "course"


class CourseCreateView(generic.CreateView):
    template_name = "lecturer/course_creation.html"
    queryset = Course.objects.all()
    form_class = CourseForm

    def get_success_url(self):
        return reverse("teach:course-list")


class CourseUpdateView(generic.UpdateView):
    template_name = "lecturer/course_update.html"
    queryset = Course.objects.all()
    form_class = CourseForm

    def get_success_url(self):
        return reverse("teach:course-list")


class CourseDeleteView(generic.DeleteView):
    template_name = "lecturer/course_delete.html"
    queryset = Course.objects.all()

    def get_success_url(self):
        return reverse("teach:course-list")







