from django.contrib import admin
from .models import Priority, Task

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('priority', 'title')


admin.site.register(Priority)
admin.site.register(Task, TaskAdmin)
