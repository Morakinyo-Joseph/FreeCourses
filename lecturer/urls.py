from django.urls import path
from lecturer import views

app_name = "lecturer"

urlpatterns = [
    path("", views.course_list, name="course-list"),
    path("create/", views.course_create, name="course-create"),
    path("<int:pk>", views.course_detail, name="course-detail"),
    path("<int:pk>/update/", views.course_update, name="course-update"),
    path("<int:pk>/delete/", views.course_delete, name="course-delete"),
]
