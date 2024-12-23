from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from .form import *
from django.contrib.auth.decorators import login_required
from django.http import Http404
# from .forms import * 

# Create your views here.
def home(request):
    projects = boards.objects.all()
    return render(request , 'home.html',{'projects':projects})
def boards_list(request,board_id):
    projects_list = get_object_or_404(boards, pk=board_id)
    return render(request , 'boards_list.html', {'projects_list':projects_list, 'board_id': board_id})
def add_board(request,board_id):
    projects_list = get_object_or_404(boards, pk=board_id)if board_id else None
    if request.method == 'POST':
        boards.objects.create(
            project_name=request.POST['project_name'],
            project_description=request.POST['description'],
            project_manager=request.POST['project_manager'],
            created_by=request.user)
        return redirect('boards_list', board_id=board_id)
    return render(request, 'add_board.html', {'board_id':board_id, 'projects_list':projects_list})
