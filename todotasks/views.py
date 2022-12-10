from asyncio import Task
from multiprocessing import context
from django.db.models import Q
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
from .models import Todo
from .forms import MyUserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import *
# Create your views here.


def home(request):
    # user = User.objects.get(id=pk)
    # user = request.id
    tasks = Todo.objects.filter(creator=request.user.id)
    q = request.GET.get('q') if request.GET.get('q') is not None else ' '
    task= Todo.objects.filter(
        # Q(creator__icontains=query) | 
        Q(title__icontains=q) |
        Q(body__icontains=q)

    )
    # tasks = Task.objects.filter(user)
    # tasks = Task.objects.filter(user=request.user.id)
    # tasks = Todo.objects.all()

    context = {'tasks': tasks, 'task': task}
    return render(request, 'todotasks/home.html', context)

def loginPage(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect ('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        
        else:
            messages.error(request, 'Username or Password incorrect')

    context = {'page': page }
    return render(request, 'todotasks/login_register.html', context)

def registerPage(request):
    form = MyUserCreationForm()
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Please check your details, one of them or both is/are wrong!')
    context = {'form': form}
    return render(request, 'todotasks/login_register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')


@login_required(login_url='login')
def AddTask(request):
    # tasks = Todo.objects.all()
    # tasks=()
    # form = TaskForm()

    # if request.method == 'POST':
    #     new_task=TaskForm(request.POST)
    #     # form.creator= request.user
    #     if new_task.is_valid:
    #         tasks = new_task.save(commit=False)
    #         tasks.user=request.user
    #         tasks.save()
    #         # form.creator= request.user
    #         return redirect('home')
    #     else:
    #         new_task = TaskForm()

    form = TaskForm(request.POST)
    tasks=Todo.objects.all()
    if form.is_valid():
        tasks = form.save(commit=False)
        tasks.creator = request.user
        tasks.save()
        return redirect('home')

    context = {'tasks': tasks, 'form':form}
    return render(request, 'todotasks/add-task.html', context)

@login_required(login_url='login')
def UpdateTask(request, pk):
    task = Todo.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == 'POST':
        task=TaskForm(request.POST, instance=task)
        if form.is_valid:
            task.save()
            return redirect('home')

    context = {'task': task, 'form': form}
    return render(request, 'todotasks/update-task.html', context)

@login_required(login_url='login')
def TaskPage(request, pk):
    task = Todo.objects.get(id=pk)

    context={'task': task}

    return render(request, 'todotasks/task.html', context)

@login_required(login_url='login')
def DelTask(request, pk):
    task = Todo.objects.get(id=pk)
     
    if request.method == 'POST':
        task.delete()
        return redirect('/')

    context = {'task':task}
    return render(request, 'todotasks/delete-task.html', context)

@login_required(login_url='login')
def Counter(request):

    return render(request, 'todotasks/sentanalyzer.html')

@login_required(login_url='login')
def WordAnalysis(request):
    text = request.POST['word']
    total_word = len(text.split())
    word_no_wo_space =len(text.replace(" ", ""))
    word_no = len(text)

    context = {'text':text, 'total_word': total_word, 'word_no': word_no, 'word_no_wo_space':word_no_wo_space}

    return render(request, 'todotasks/wordanalysis.html', context)
