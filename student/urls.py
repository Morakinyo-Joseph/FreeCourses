from django.urls import path
from student import views

app_name = 'student'
urlpatterns = [
    path("studentsignup", views.studentsignup, name="SignUp"),
    path("studentlogin", views.studentlogin, name="Login"),
]
