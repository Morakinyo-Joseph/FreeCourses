from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime


class User(AbstractUser):
    pass


class Lecturer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    confirm = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class Course(models.Model):

    TOPIC_CHOICES = (
        ("", "Select"),
        ("History", "History"),
        ("Chemistry", "Chemistry"),
        ("Computer", "Computer")
    )

    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
    category = models.CharField(choices=TOPIC_CHOICES, max_length=100)

    topic = models.CharField(max_length=250)
    content = models.CharField(max_length=2500)

    date_created = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f"{self.lecturer}: {self.topic}"

