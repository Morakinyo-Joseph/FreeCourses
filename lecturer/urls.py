from django.urls import path
from . import views

app_name = "lecturer"

urlpatterns = [
    path("", views.course_list, name="course-list"),
    path("<int:pk>", views.course_detail, name="course-detail"),
    path("<int:pk>/update/", views.course_update, name="course-update"),
    path("<int:pk>/delete/", views.course_delete, name="course-delete"),
    path("create/", views.course_creation, name="course-create"),
]
