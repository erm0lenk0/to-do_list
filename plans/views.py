from django.utils import timezone


from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic, View

from plans.forms import TaskForm
from plans.models import Task, Tag


def index(request):
    tasks = Task.objects.prefetch_related('tags').order_by("is_done", "-datetime")
    return render(request, "plans/index.html", {"tasks": tasks})


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = "plans/task_form.html"
    success_url = reverse_lazy("plans:index")

    def form_valid(self, form):
        task = form.save(commit=False)
        duration = form.cleaned_data['duration_input']
        task.deadline = timezone.now() + duration
        task.save()
        form.save_m2m()
        return super().form_valid(form)


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "plans/task_form.html"
    success_url = reverse_lazy("plans:index")

class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "plans/task_confirm_delete.html"
    success_url = reverse_lazy("plans:index")

class ToggleAssignToTaskView(View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.is_done = not task.is_done
        task.save()
        return redirect("plans:index")


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
