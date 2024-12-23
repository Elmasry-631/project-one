from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(boards)
class BoardAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'project_description', 'project_manager', 'created_at', 'created_by')
    