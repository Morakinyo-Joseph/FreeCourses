from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
<<<<<<< HEAD
from lecturer import views as lecturer_views
from student import views as student_views
=======
from register import views as v

>>>>>>> c97dd558a16ad29d17ae430f3e3d253d017f9629

urlpatterns = [
    path('admin/', admin.site.urls),

<<<<<<< HEAD
    path('teach/', include('lecturer.urls', namespace='teach')),

    path('learn/', include('student.urls', namespace='learn')),
=======
    path("register", v.register, name="register"),
    path('', v.landing_page, name='landing_page'),
    path('homepage', v.homepage, name="homepage"),

    path('teach/', include('lecturer.urls', namespace="teach")),

    # path('learn/', include('student.urls', namespace="learn")),
>>>>>>> c97dd558a16ad29d17ae430f3e3d253d017f9629

    path('login/', LoginView.as_view(), name="login"),

    path('logout/', LogoutView.as_view(), name="logout"),
<<<<<<< HEAD

    path('signup/', lecturer_views.signup, name="signup"),

    path('studentsignup/', student_views.studentsignup, name="Student_signup"),

    path('studentlogin/', student_views.studentlogin, name="Student_login")
=======
>>>>>>> c97dd558a16ad29d17ae430f3e3d253d017f9629
]

