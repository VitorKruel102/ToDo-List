from django.urls import path

from tasks.views import helloWorld, taskList, taskView, yourName, newTask

urlpatterns = [
    path('helloWorld/', helloWorld),
    path('', taskList, name='task-list'),
    path('task/<int:id>', taskView, name='task-list'),
    path('newtask/', newTask, name='new-task'),
    path('yourname/<str:name>', yourName, name='your-name')
]