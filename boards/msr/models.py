from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class boards(models.Model):
    project_name = models.CharField(max_length=20)
    project_description = models.TextField(max_length=100)
    project_manager = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.project_name
class Tasks(models.Model):
    task_name = models.CharField(max_length=20)