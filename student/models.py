from unicodedata import name
from django.db import models
from datetime import datetime

# Create your models here.

class Student(models.Model):
    Fname = models.CharField("First Name",max_length=35)
    Lname = models.CharField("Last Name",max_length=35)
    date_registered = models.DateTimeField(default=datetime.now)
    date_of_birth = models.DateField(null=False)
    student_email = models.EmailField("Student Email")

    def __str__(self):
        return self.Fname