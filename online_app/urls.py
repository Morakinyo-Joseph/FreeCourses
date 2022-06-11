from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from lecturer import views as lecturer_views
from student import views as student_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('teach/', include('lecturer.urls', namespace='teach')),

    path('learn/', include('student.urls', namespace='learn')),

    path('login/', LoginView.as_view(), name="login"),

    path('logout/', LogoutView.as_view(), name="logout"),

    path('signup/', lecturer_views.signup, name="signup"),

    path('studentsignup/', student_views.studentsignup, name="Student_signup"),

    path('studentlogin/', student_views.studentlogin, name="Student_login")
]
