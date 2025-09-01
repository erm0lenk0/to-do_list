from django.urls import path

from .views import (
    index,
    TegListView,
)

app_name = "plans"

urlpatterns = [
    path("", index, name="index"),
    path("teg/", TegListView.as_view(), name="teg_list"),
]