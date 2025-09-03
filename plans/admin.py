from django.contrib import admin
from plans.models import Task, Tag


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('content', 'is_done', 'datetime', 'deadline')
    list_filter = ('is_done', 'datetime', 'deadline', 'tags')
    search_fields = ('content',)
    ordering = ('-datetime',)


admin.site.register(Tag)
