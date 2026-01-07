from django.urls import path
from .views import task_list_create, task_delete

urlpatterns = [
    path('tasks/', task_list_create),
    path('tasks/<int:task_id>/', task_delete),
]
