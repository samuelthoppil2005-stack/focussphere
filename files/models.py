from django.db import models
from django.contrib.auth.models import User
from subjects.models import Subject


class StudyMaterial(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    title = models.CharField(max_length=200)

    file = models.FileField(upload_to="study_materials/")

    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title   