from django.shortcuts import render
from django.views import generic

from todo.models import Task, Tag


def index(request):
    tasks = Task.objects.all().prefetch_related("tags")
    context = {"tasks": tasks}

    return render(request, "todo/index.html", context=context)


class TagListView(generic.ListView):
    model = Tag

