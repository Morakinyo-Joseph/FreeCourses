from django.shortcuts import render, redirect, reverse
from .models import Course, Lecturer
from .forms import CourseForm
from django.contrib import messages
from django.views import generic


def course_list(request):
    course = Course.objects.all()
    return render(request, 'lecturer/course_list.html', {"course": course})


class CourseCreateView(generic.CreateView):
    template_name = "lecturer/course_creation.html"
    queryset = Course.objects.all()
    form_class = CourseForm

    def get_success_url(self):
        return reverse("teach:course-list")


def course_detail(request, pk):
    course = Course.objects.get(id=pk)
    return render(request, 'lecturer/course_detail.html', {"course": course})


def course_update(request, pk):
    course = Course.objects.get(id=pk)
    return render(request, 'lecturer/course_update.html', {"course": course})


def course_delete(request, pk):
    course = Course.objects.get(id=pk)
    course.delete()
    return redirect("/teach")








