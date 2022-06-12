from unicodedata import name
from django.db import models
from datetime import datetime

from django.forms import PasswordInput

# Create your models here.

class Student(models.Model):
    Fname = models.CharField("First Name",max_length=35)
    Lname = models.CharField("Last Name",max_length=35)
    Username = models.CharField("User Name", max_length=35)
    password = models.CharField("Password", max_length=30)
    password2 = models.CharField("Password Again", max_length=30)
    date_registered = models.DateTimeField(default=datetime.now)
    date_of_birth = models.DateField(null=False)
    student_email = models.EmailField("Student Email")

    def __str__(self):
        return self.Fname