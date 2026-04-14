from django.shortcuts import render , redirect, get_object_or_404
from .models import Assignment
from subjects.models import Subject
from django.contrib.auth.decorators import login_required

@login_required
def assignments_view(request):

    assignments = Assignment.objects.filter(user=request.user)

    context = {
        'assignments': assignments
    }

    return render(request, 'assignments/assignments.html', context)

def add_assignment(request):
    
    if request.method == "POST":

        subject_name = request.POST.get("subject")

        subject, created = Subject.objects.get_or_create(
            name=subject_name,
            user=request.user
        )

        Assignment.objects.create(
            user=request.user,
            subject=subject,
            title=request.POST.get("title"),
            due_date=request.POST.get("due_date")
        )

        return redirect("assignments")

    return render(request, "assignments/add_assignment.html")


def edit_assignment(request, id):

    assignment = get_object_or_404(Assignment, id=id, user=request.user)

    if request.method == "POST":

        assignment.subject = request.POST.get("subject")
        assignment.title = request.POST.get("title")
        assignment.due_date = request.POST.get("due_date")
        assignment.completed = request.POST.get("completed") == "True"

        assignment.save()

        return redirect("assignments")

    return render(request, "assignments/edit_assignment.html", {"assignment": assignment})


def delete_assignment(request, id):

    assignment = get_object_or_404(Assignment, id=id, user=request.user)

    assignment.delete()

    return redirect("assignments")