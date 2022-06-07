from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from lecturer.views import SignupView


urlpatterns = [
    path('admin/', admin.site.urls),

    path('teach/', include('lecturer.urls', namespace="teach")),

    path('learn/', include('student.urls', namespace = "learn")),

    path('login/', LoginView.as_view(), name="login"),

    path('logout/', LogoutView.as_view(), name="logout"),

    path('signup/', SignupView.as_view(), name="signup"),
]
