from django.contrib import admin

from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ['id','title','description','complete','user']
    ordering = ('id',)
    search_fields = ('title',)

admin.site.register(Task, TaskAdmin)
