from django.shortcuts import render, redirect , get_object_or_404
from .models import Task
from django.contrib.auth.decorators import login_required

@login_required
def tasks_view(request):

    tasks = Task.objects.filter(user=request.user)

    context = {
        'tasks': tasks
    }

    return render(request, 'tasks/tasks.html', context)

def add_task(request):
    
    if request.method == "POST":

        title = request.POST.get("title")
        due_date = request.POST.get("due_date")

        Task.objects.create(
            user=request.user,
            title=title,
            due_date=due_date
        )

        return redirect("tasks")

    return render(request, "tasks/add_task.html")


def edit_task(request, id):
    
    task = get_object_or_404(Task, id=id, user=request.user)

    if request.method == "POST":

        task.title = request.POST.get("title")
        task.due_date = request.POST.get("due_date")

        task.save()

        return redirect("tasks")

    return render(request, "tasks/edit_task.html", {"task": task})


def delete_task(request, id):

    task = get_object_or_404(Task, id=id, user=request.user)

    task.delete()

    return redirect("tasks")