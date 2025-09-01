from django.shortcuts import render
from django.views import generic

from plans.models import Task, Tag


def index(request):
    tasks = Task.objects.all().order_by("is_done", "-datetime")
    return render(request, "plans/index.html", {"tasks": tasks})


class TegListView(generic.ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "plans/teg_list.html"





