from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from subjects.models import Subject


def notes_view(request):

    notes = Note.objects.filter(user=request.user).order_by("-created_at")

    return render(request, "notes/notes.html", {"notes": notes})


def add_note(request):

    if request.method == "POST":

        subject_name = request.POST.get("subject")

        subject, created = Subject.objects.get_or_create(
            name=subject_name,
            user=request.user
        )

        Note.objects.create(
            user=request.user,
            subject=subject,
            title=request.POST.get("title"),
            content=request.POST.get("content")
        )

        return redirect("notes")

    return render(request, "notes/add_note.html")

def view_note(request, id):
    
    note = get_object_or_404(Note, id=id, user=request.user)

    return render(request, "notes/view_note.html", {"note": note})

def edit_note(request, id):

    note = get_object_or_404(Note, id=id, user=request.user)

    if request.method == "POST":

        subject_name = request.POST.get("subject")

        subject, created = Subject.objects.get_or_create(
            name=subject_name,
            user=request.user
        )

        note.subject = subject
        note.title = request.POST.get("title")
        note.content = request.POST.get("content")

        note.save()

        return redirect("notes")

    return render(request, "notes/edit_note.html", {"note": note})


def delete_note(request, id):

    note = get_object_or_404(Note, id=id, user=request.user)

    note.delete()

    return redirect("notes")