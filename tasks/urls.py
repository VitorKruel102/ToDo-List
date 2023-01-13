from django.urls import path

from tasks.views import helloWorld

urlpatterns = [
    path('helloWorld/', helloWorld),
]