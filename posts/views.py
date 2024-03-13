
from django.shortcuts import render, redirect

from .models import *
from .forms import *

# Create your views here.
def index(request):
    posts = Post.objects.all()

    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")        

    context = {'posts':posts, 'form':form} #dictionary

    return render(request, 'index.html', context)

def update_blog(request, pk):
    posts = Post.objects.get(id=pk)

    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, instance=posts)
        if form.is_valid():
            form.save()
        return redirect("/")        

    context = {'form':form, 'posts':post}

    return render(request, 'update.html', context)

def post(request, pk):
    posts = Post.objects.get(id=pk)
    return render(request, 'posts.html', {'posts':posts})

def delete_blog(request, pk):
    item = Post.objects.get(id=pk)
    item.delete()
    return redirect('/')
    
    

"""def update_blog(request, pk):
    posts= Post.objects.get(id=pk)
    return render(request, 'update.html', {'posts':posts})

    
def delete_blog(request, pk):
    item = Post.objects.get(id=pk)
    
    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {'item':item}
    return render(request, 'delete.html', context)"""


def todo(request):
    tasks = Task.objects.all()

    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("list")

    context = {'tasks':tasks, 'form':form} #dictionary 

    #return HttpResponse("hello world")
    return render(request, 'tasks/list.html', context) 

def updateTask(request, pk):
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect("/")
    
    context = {'form':form, 'task':task}

    return render(request, 'tasks/update_task.html', context)

def deleteTask(request, pk):
    item = Task.objects.get(id=pk)
    
    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {'item':item}
    return render(request, 'tasks/delete.html', context)

def searchbar(request):
   if request.method == 'GET':
    search = request.GET.get('search_bar')
    post = Task.objects.all().filter(title__contains=search)
    return render(request, 'tasks/searchbar.html', {'post': post})