"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('todos/', include('todos.urls')),
    path('', include('todos.urls')),
]

# if 'todos.urls' not found, add the following code instead
# urlpatterns += [
#     path('todos/hello/', views.hello_world, name='hello_world'),
# ]
# Note: Make sure to import views if using the above code
# from todos import views
# from todos.views import hello_world
# However, the preferred way is to include the todos.urls module

# This setup allows for better organization and scalability of the project.