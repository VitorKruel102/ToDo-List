from django.urls import path

from tasks.views import helloWorld, taskList, taskView, yourName, newTask, editTask

urlpatterns = [
    path('helloWorld/', helloWorld),
    path('', taskList, name='task-list'),
    path('task/<int:id>', taskView, name='task-list'),
    path('newtask/', newTask, name='new-task'),
    path('edit/<int:id>', editTask, name='edit'), #O Id é utilizado para mostar os dados atuais para saber o que vai editar.
    path('yourname/<str:name>', yourName, name='your-name')
]