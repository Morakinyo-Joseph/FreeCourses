from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from datetime import datetime


class User(AbstractUser):
    pass


class Lecturer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Course(models.Model):

    TOPIC_CHOICES = (
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


# def post_user_to_lecturer_create(sender, instance, created, **kwargs):
#     if created:
#         Lecturer.objects.create(user=instance)
#
#
# post_save.connect(post_user_to_lecturer_create, sender=User)
