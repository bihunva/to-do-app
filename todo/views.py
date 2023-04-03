from django.shortcuts import render

from todo.models import Task


def index(request):
    tasks = Task.objects.all()
    context = {"tasks": tasks}

    return render(request, "todo/index.html", context=context)
