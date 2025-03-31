from django.urls import path
from . import views

from django.urls import path

urlpatterns = [
    path('task-list', views.task_list, name='task-list'),
    path('signup/', views.signup, name='signup'),
    path('task/edit/<int:task_id>/', views.edit_task, name='edit-task'),
    path('task/delete/<int:task_id>/', views.delete_task, name='delete-task'),
    path('task/toggle/<int:task_id>/', views.toggle_task, name='toggle-task'),
    path("send-email/", views.send_test_email, name='send-email'),
]