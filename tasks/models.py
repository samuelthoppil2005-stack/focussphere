from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):

    STATUS = [
        ('PENDING', 'Pending'),
        ('DONE', 'Done'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    due_date = models.DateField(null=True, blank=True)

    status = models.CharField(max_length=10, choices=STATUS, default='PENDING')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title