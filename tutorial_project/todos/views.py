from django.shortcuts import render
from django.http import HttpResponse

# Views here.

def hello_world(request):
    # return render(request, 'hello.html', {'message': 'Hello, World!'})
    return HttpResponse("Hello, World!")