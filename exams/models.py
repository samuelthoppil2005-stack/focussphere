from django.db import models
from django.contrib.auth.models import User
from subjects.models import Subject
from datetime import date

class Exam(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    exam_name = models.CharField(max_length=200, blank=True)
    exam_date = models.DateField()

    @property
    def days_remaining(self):

        today = date.today()
        remaining = (self.exam_date - today).days

        return remaining

    created_at = models.DateTimeField(auto_now_add=True)

    def days_remaining(self):
        today = date.today()
        return (self.exam_date - today).days

    def __str__(self):
        return self.title