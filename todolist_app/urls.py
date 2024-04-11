from django.urls import path
from .views import task_list, create_task, edit_task, delete_task, toggle_complete

urlpatterns = [
    path('', task_list, name='task_list'),
    path('create-task', create_task, name='create_task'),
    path('edit-task/<int:pk>', edit_task, name='edit_task'),
    path('delete-task/<int:pk>', delete_task, name='delete_task'),
    path('toggle-complete/<int:pk>', toggle_complete, name='toggle_complete'),
]