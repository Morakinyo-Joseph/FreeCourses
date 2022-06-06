from django.urls import path
from . import views

app_name = "lecturer"

urlpatterns = [
    path("", views.CourseListView.as_view(), name="course-list"),
    path("<int:pk>", views.CourseDetailView.as_view(), name="course-detail"),
    path("<int:pk>/update/", views.CourseUpdateView.as_view(), name="course-update"),
    path("<int:pk>/delete/", views.CourseDeleteView.as_view(), name="course-delete"),
    path("create/", views.CourseCreateView.as_view(), name="course-create"),
]
