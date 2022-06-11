from django import forms
from .models import Course
from django.contrib.auth import get_user_model

User = get_user_model()


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = (
            "lecturer",
            "category",
            "topic",
            "content",
        )
