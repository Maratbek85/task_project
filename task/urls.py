from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('add/', views.add_tasks, name='add_task'),
    path('complete/<int:task_id>/', views.completed_task, name='completed_task'),
]