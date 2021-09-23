from django.http import HttpResponse
from django.shortcuts import render
from .models import Task
from .forms import TaskForm


def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/index.html', {'title':'Главная страница сайта', 'tasks': tasks})


def about(request):
    return render(request, 'main/about.html')


def createTask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return index(request)
    form = TaskForm()
    context = {
        "form": form
    }
    return render(request, 'main/createTask.html', context)


def detailsTask(request, pk):
    task = Task.objects.get(id=pk)
    return render(request, "main/detailTask.html", {"task": task})


def detailsTaskk(request, pk):
    task = Task.objects.get(id=1)
    return render(request, "main/detailTask.html", {"task": task})