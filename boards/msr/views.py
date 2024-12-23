from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.http import Http404
# Create your views here.
def home(request):
    projects = boards.objects.all()
    return render(request , 'home.html',{'projects':projects})
def boards_list(request,board_id):
    projects_list = get_object_or_404(boards, pk=board_id)
    return render(request , 'boards_list.html', {'projects_list':projects_list, 'board_id': board_id})
@login_required
def add_board(request,board_id):
    projects_list = get_object_or_404(boards, pk=board_id)if board_id else None
    form = new_board()
    user = User.objects.first()
    if request.method == 'POST':
        form =new_board(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.projects_list = projects_list
            topic.created_by = user
            topic.save()
            return redirect('boards_list', board_id=board_id)
        else:
            form = new_board()
    return render(request, 'add_board.html', {'board_id':board_id, 'projects_list':projects_list, 'form':form})
