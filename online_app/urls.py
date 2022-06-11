from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from register import views as v


urlpatterns = [
    path('admin/', admin.site.urls),

    path("register", v.register, name="register"),
    path('', v.landing_page, name='landing_page'),
    path('homepage', v.homepage, name="homepage"),

    path('teach/', include('lecturer.urls', namespace="teach")),

    # path('learn/', include('student.urls', namespace="learn")),

    path('login/', LoginView.as_view(), name="login"),

    path('logout/', LogoutView.as_view(), name="logout"),
]

