from django.urls import path

from .views import (
    index,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    ToggleAssignToTaskView,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
)

app_name = "plans"

urlpatterns = [
    path("", index, name="index"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path("task/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("task/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("task/<int:pk>/toggle-assign/", ToggleAssignToTaskView.as_view(), name="toggle-assign-task"),
    path("tag/", TagListView.as_view(), name="tag-list"),
    path("tag/create/", TagCreateView.as_view(), name="tag-create"),
    path("tag/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tag/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),

]
