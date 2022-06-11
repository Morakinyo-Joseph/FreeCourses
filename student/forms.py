from pyexpat import model
from django import forms
from student.models import *
from django.contrib.auth import get_user_model

User = get_user_model

class StudentsignupForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = (
            "Fname",
            "Lname",
            "Username",
            "password1",
            "password2",
            "date_of_birth",
            "student_email",
        )

        widgets = {
            'password1': forms.PasswordInput(),
            'password2': forms.PasswordInput(),
        }


class StudentloginForm(forms.Form):
     class Meta:
        username = forms.CharField(max_length=20)
        password = forms.CharField(max_length=20, widget=PasswordInput)