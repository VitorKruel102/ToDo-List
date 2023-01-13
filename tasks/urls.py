from django.urls import path

from tasks.views import helloWorld, taskList, yourName

urlpatterns = [
    path('helloWorld/', helloWorld),
    path('', taskList, name='task-list'),
    path('yourname/<str:name>', yourName, name='your-name')
]