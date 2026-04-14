from django.shortcuts import render, redirect, get_object_or_404
from .models import Exam
from subjects.models import Subject


def exams_view(request):

    exams = Exam.objects.filter(user=request.user).order_by("exam_date")

    return render(request, "exams/exams.html", {"exams": exams})


def add_exam(request):

    if request.method == "POST":

        subject_name = request.POST.get("subject")

        subject, created = Subject.objects.get_or_create(
            name=subject_name,
            user=request.user
        )

        Exam.objects.create(
            user=request.user,
            subject=subject,
            exam_name=request.POST.get("exam_name"),
            exam_date=request.POST.get("exam_date")
        )

        return redirect("exams")

    return render(request, "exams/add_exam.html")

def edit_exam(request, id):
    
    exam = get_object_or_404(Exam, id=id, user=request.user)

    if request.method == "POST":

        subject_name = request.POST.get("subject")

        subject, created = Subject.objects.get_or_create(
            name=subject_name,
            user=request.user
        )

        exam.subject = subject
        exam.exam_name = request.POST.get("exam_name")
        exam.exam_date = request.POST.get("exam_date")

        exam.save()

        return redirect("exams")

    return render(request, "exams/edit_exam.html", {"exam": exam})


def delete_exam(request, id):

    exam = get_object_or_404(Exam, id=id, user=request.user)

    exam.delete()

    return redirect("exams")