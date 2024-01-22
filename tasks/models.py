from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Priority(models.Model):
    name = models.CharField(max_length=10)
    
    def __str__(self) -> str:
        return self.name 


class Task(models.Model):
    priority = models.ForeignKey(Priority, related_name='tasks', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    image = models.ImageField(upload_to="images", blank=True, null=True)
    created_by = models.ForeignKey(User, related_name="tasks", on_delete=models.CASCADE)
    is_complete = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)