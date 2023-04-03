from django.shortcuts import render

from todo.models import Task


def index(request):
    tasks = Task.objects.all().prefetch_related("tags")
    context = {"tasks": tasks}

    return render(request, "todo/index.html", context=context)
