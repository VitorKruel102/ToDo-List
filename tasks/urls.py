from django.urls import path

from tasks.views import helloWorld, taskList, taskView, yourName, newTask, editTask, deleteTask

urlpatterns = [
    path('helloWorld/', helloWorld),
    path('', taskList, name='task-list'),
    path('task/<int:id>', taskView, name='task-list'),
    path('newtask/', newTask, name='new-task'),
    path('edit/<int:id>', editTask, name='edit-task'), #O Id é utilizado para mostar os dados atuais para saber o que vai editar.
    path('delete/<int:id>', deleteTask, name='delete-task'),
    path('yourname/<str:name>', yourName, name='your-name')
]