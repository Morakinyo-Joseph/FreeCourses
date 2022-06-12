from django.urls import path
from student import views

app_name = 'student'

urlpatterns = [
    
    path("", views.course_view, name="course-view"),

    path("studentsignup", views.studentsignup, name="signup"),
    path("studentlogin", views.studentlogin, name="login"),
]
