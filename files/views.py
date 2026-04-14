from django.shortcuts import render, redirect, get_object_or_404
from .models import StudyMaterial
from subjects.models import Subject


def files_view(request):

    files = StudyMaterial.objects.filter(user=request.user)

    return render(request, "files/files.html", {"files": files})


def upload_file(request):
    
    if request.method == "POST":

        subject_name = request.POST.get("subject")

        subject, created = Subject.objects.get_or_create(
            name=subject_name,
            user=request.user
        )

        StudyMaterial.objects.create(
            user=request.user,
            subject=subject,
            title=request.POST.get("title"),
            file=request.FILES["file"]
        )

        return redirect("files")

    return render(request, "files/upload_file.html")


def delete_file(request, id):

    file = get_object_or_404(StudyMaterial, id=id, user=request.user)

    file.delete()

    return redirect("files")