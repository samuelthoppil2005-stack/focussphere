from django.db import models
from django.contrib.auth.models import User
from subjects.models import Subject

class Attendance(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    total_classes = models.IntegerField()

    attended_classes = models.IntegerField()

    updated_at = models.DateTimeField(auto_now=True)

    @property
    def percentage(self):

        if self.total_classes == 0:
            return 0

        return round((self.attended_classes / self.total_classes) * 100, 2) 
    
@property
def needed_for_75(self):

    attended = self.attended_classes
    total = self.total_classes

    if total == 0:
        return 0

    needed = 0

    while (attended + needed) / (total + needed) < 0.75:
        needed += 1

    return needed   