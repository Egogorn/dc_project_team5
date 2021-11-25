"""dc_project_team5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path

from core import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("profile", views.profile, "profile"),
    path('login', views.login_page, "login_page"),
    path('register', views.register_page, "register_page"),
    path('dashboard', views.dashboard, "dashboard"),
    path('deadlines', views.deadlines, 'deadlines'),
    path('tasks', views.tasks, 'tasks'),
    path('solutions', views.solutions, 'solutions'),
    path('solution', views.solution_page, 'solution_page'),
    path('deadline', views.deadline_page, 'deadline_page'),
    path('task', views.task_page, 'task_page'),
    path('group', views.group_page, 'group_page'),
    path('person', views.person_page, 'person_page'),
    path('create_task', views.create_task, 'create_task'),
    path('give_task', views.give_task, 'give_task'),
]
