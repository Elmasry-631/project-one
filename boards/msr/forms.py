from django import forms
from .models import boards

class new_board(forms.ModelForm):
    # project_name = forms.CharField(max_length=20, label = 'Project Name')
    # project_description = forms.CharField( widget=forms.Textarea, max_length=200, label = 'Project Description')
    # project_manager = forms.CharField( max_length=20, label='Project Manager')
    class Meta:
        model = boards
        fields = ('project_name','project_description','project_manager')

    
