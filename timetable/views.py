from django.shortcuts import render, redirect, get_object_or_404
from .models import Timetable
from subjects.models import Subject
from django.contrib.auth.decorators import login_required

@login_required
def timetable_view(request):

    timetable = Timetable.objects.filter(user=request.user)

    context = {
        'timetable': timetable
    }

    return render(request, 'timetable/timetable.html', context)

def add_timetable(request):
    
    if request.method == "POST":

        subject_name = request.POST.get("subject")

        subject, created = Subject.objects.get_or_create(
            name=subject_name,
            user=request.user
        )

        Timetable.objects.create(
            user=request.user,
            day=request.POST.get("day"),
            subject=subject,
            start_time=request.POST.get("start_time"),
            end_time=request.POST.get("end_time"),
            room=request.POST.get("room"),
        )

        return redirect("timetable")

    return render(request, "timetable/add_timetable.html")

def edit_timetable(request, id):

    period = get_object_or_404(Timetable, id=id, user=request.user)

    if request.method == "POST":

        subject_name = request.POST.get("subject")

        subject, created = Subject.objects.get_or_create(
            name=subject_name
        )

        period.day = request.POST.get("day")
        period.subject = subject
        period.start_time = request.POST.get("start_time")
        period.end_time = request.POST.get("end_time")
        period.room = request.POST.get("room")

        period.save()

        return redirect("timetable")

    return render(request, "timetable/edit_timetable.html", {"period": period})


def delete_timetable(request, id):

    period = get_object_or_404(Timetable, id=id, user=request.user)

    period.delete()

    return redirect("timetable")