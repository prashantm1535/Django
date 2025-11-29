from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_world_view, name='hello_world'),
    path('todos/', views.hello_python_view, name='This is the todo list.'),
]