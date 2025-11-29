from django.shortcuts import render
from django.http import HttpResponse

# Views here.

def hello_world_view(request):
    # return render(request, 'hello.html', {'message': 'Hello, World!'})
    return HttpResponse("Hello, World!")

def hello_python_view(request):
    return HttpResponse("This is the todo list.")