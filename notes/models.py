from django.db import models
from django.contrib.auth.models import User
from subjects.models import Subject


class Note(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    title = models.CharField(max_length=200)

    content = models.TextField()

    pinned = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)