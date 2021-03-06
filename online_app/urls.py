from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from lecturer.views import homepage, landing_page



urlpatterns = [
    path('admin/', admin.site.urls),

    path('', landing_page, name='landing_page'),
    path('homepage', homepage, name="homepage"),

    path('teach/', include('lecturer.urls', namespace="teach")),
    path('learn/', include('student.urls', namespace="learn")),

]

