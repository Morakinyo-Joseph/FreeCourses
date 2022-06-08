from django import forms
from .models import Course
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model

User = get_user_model()


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = (
            "lecturer",
            "category",
            "topic",
        )

#
# class CustomUserCreationForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ("username", "email", "first_name", "last_name", "password1", "password2")
#         field_classes = {"username": UsernameField}
