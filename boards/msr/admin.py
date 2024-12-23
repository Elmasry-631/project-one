from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(boards)
class BoardAdmin(admin.ModelAdmin):
    list_display = ('id','project_name', 'project_description', 'project_manager', 'created_at', 'created_by')
    list_filter = ('project_manager','project_name','created_by')
    search_fields = ('project_name', 'created_by', 'project_manager')
    ordering = ('-created_at',)