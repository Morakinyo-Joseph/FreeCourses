from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from lecturer.views import signup

urlpatterns = [
    path('admin/', admin.site.urls),

    path('teach/', include('lecturer.urls', namespace="teach")),

    path('login/', LoginView.as_view(), name="login"),

    path('logout/', LogoutView.as_view(), name="logout"),

    path('signup/', signup, name="signup"),
]
