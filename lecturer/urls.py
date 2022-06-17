from django.urls import path
from lecturer import views
from lecturer.views import logging_in, register, logging_out

app_name = "lecturer"

urlpatterns = [
    path("", views.course_list, name="course-list"),

    path("lecturer_course", views.courses, name="courses"),

    path("create/", views.course_create, name="course-create"),
    path("<int:pk>", views.course_detail, name="course-detail"),
    path("<int:pk>/update/", views.course_update, name="course-update"),
    path("<int:pk>/delete/", views.course_delete, name="course-delete"),
    path("lecturer_signup", register,  name="signup"),
    path("lecturer_login", logging_in, name="login"),
    path("lecturer_logout", logging_out, name="logout"),
]
