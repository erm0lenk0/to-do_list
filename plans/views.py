from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from plans.models import Task, Tag


def index(request):
    tasks = Task.objects.all().order_by("is_done", "-datetime")
    return render(request, "plans/index.html", {"tasks": tasks})


class TaskCreateView(generic.ListView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("plans:index")
    template_name = "plans/task_form.html"

class TaskUpdateView(generic.DetailView):
    model = Task
    fields = "__all__"
    template_name = "plans/task_form.html"
    success_url = reverse_lazy("plans:index")

class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "plans/task_confirm_delete.html"
    success_url = reverse_lazy("plans:index")

# class ToggleAssignToTaskView(generic.DetailView):
#     model = Task
#     fields = "__all__"


class TagListView(generic.ListView):
    model = Tag
    context_object_name = "tag_list"
    template_name = "plans/tag_list.html"

class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("plans:tag-list")
    template_name = "plans/tag_form.html"

class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    template_name = "plans/tag_form.html"
    success_url = reverse_lazy("plans:tag-list")

class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "plans/tag_confirm_delete.html"
    success_url = reverse_lazy("plans:tag-list")
