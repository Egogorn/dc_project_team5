from django.shortcuts import render
from django.http import HttpResponse

def profile(request):
    return render(request, 'profile.html', {})


def login_page(request):
    return render(request, 'login_page.html', {})


def register_page(request):
    return render(request, 'register_page.html', {})


def dashboard(request):
    return render(request, 'dashboard.html', {})


def deadlines(request):
    return render(request, 'deadlines.html', {})


def tasks(request):
    return render(request, 'tasks.html', {})


def solutions(request):
    return render(request, 'solutions.html', {})


def solution_page(request):
    return render(request, 'solution_page.html', {})


def deadline_page(request):
    return render(request, 'deadline_page.html',{})


def task_page(request):
    return render(request, 'task_page.html', {})


def group_page(request):
    return render(request, 'group_page.html', {})


def person_page(request):
    return render(request, 'person_page.html', {})


def login_page(request):
    return render(request, 'login_page.html', {})


def create_task(request):
    return render(request, 'create_task.html', {})


def give_task(request):
    return render(request, 'give_task.html', {})
