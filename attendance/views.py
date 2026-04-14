from django.shortcuts import render, redirect, get_object_or_404
from .models import Attendance
from subjects.models import Subject
from django.contrib.auth.decorators import login_required

@login_required
def attendance_view(request):
    
    attendance = Attendance.objects.filter(user=request.user)

    total_classes = 0
    attended_classes = 0

    for a in attendance:
        total_classes += a.total_classes
        attended_classes += a.attended_classes

    if total_classes == 0:
        overall_percentage = 0
    else:
        overall_percentage = round((attended_classes / total_classes) * 100, 2)

    context = {
        "attendance": attendance,
        "overall_percentage": overall_percentage
    }

    return render(request, "attendance/attendance.html", context)
def add_attendance(request):
    
    if request.method == "POST":

        subject_name = request.POST.get("subject")

        subject, created = Subject.objects.get_or_create(
            name=subject_name,
            user=request.user
        )

        Attendance.objects.create(
            user=request.user,
            subject=subject,
            total_classes=request.POST.get("total_classes"),
            attended_classes=request.POST.get("attended_classes"),
        )

        return redirect("attendance")

    return render(request, "attendance/add_attendance.html")

def edit_attendance(request, id):
    
    attendance = get_object_or_404(Attendance, id=id, user=request.user)

    if request.method == "POST":

        subject_name = request.POST.get("subject")

        subject, created = Subject.objects.get_or_create(
            name=subject_name,
            user=request.user
        )

        attendance.subject = subject
        attendance.total_classes = request.POST.get("total_classes")
        attendance.attended_classes = request.POST.get("attended_classes")

        attendance.save()

        return redirect("attendance")

    return render(request, "attendance/edit_attendance.html", {"attendance": attendance})


def delete_attendance(request, id):

    attendance = get_object_or_404(Attendance, id=id, user=request.user)

    attendance.delete()

    return redirect("attendance")

@property
def needed_classes(self):

    attended = self.attended_classes
    total = self.total_classes

    needed = 0

    while (attended + needed) / (total + needed) < 0.75:
        needed += 1

    return needed