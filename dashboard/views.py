from django.shortcuts import render
from timetable.models import Timetable
from assignments.models import Assignment
from tasks.models import Task
from exams.models import Exam
from attendance.models import Attendance
from files.models import StudyMaterial
from django.contrib.auth.decorators import login_required
from datetime import date


@login_required
def dashboard_view(request):

    today = date.today()

    classes_today = Timetable.objects.filter(user=request.user)

    assignments = Assignment.objects.filter(
        user=request.user,
        status='PENDING'
    )

    tasks = Task.objects.filter(user=request.user, status='PENDING')

    exams = Exam.objects.filter(user=request.user)

    attendance = Attendance.objects.filter(user=request.user)

    files = StudyMaterial.objects.filter(user=request.user)[:5]

    context = {
        "classes_today": classes_today,
        "assignments": assignments,
        "tasks": tasks,
        "exams": exams,
        "attendance": attendance,
        "files": files,
    }

    return render(request, "dashboard/dashboard.html", context)