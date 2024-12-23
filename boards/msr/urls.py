from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('boards/<int:board_id>/', views.boards_list, name='boards_list'),
    path('boards/<int:board_id>/new', views.add_board, name='add_board'),
]
