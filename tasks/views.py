from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse

from django.shortcuts import render, redirect, get_object_or_404

from .models import Task
from .forms import TaskForm

# Create your views here.
@login_required
def task_list(request):
    filter_status = request.GET.get('status', 'all')

    if filter_status == 'completed':
        tasks = Task.objects.filter(user=request.user, completed=True)
    elif filter_status == 'pending':
        tasks = Task.objects.filter(user=request.user, completed=False)
    else:
        tasks = Task.objects.filter(user=request.user)

    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task-list')

    return render(request, 'tasks/task_list.html', {
        'tasks': tasks,
        'form': form,
        'filter_status': filter_status
    })

@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task-list')
        
    form = TaskForm(instance=task)
    return render(request, 'tasks/edit_task.html', {
        'form': form
    })

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.delete()
    return redirect('task-list')

@login_required
def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.completed = not task.completed
    task.save()
    return redirect('task-list')


def send_test_email(request):
    subject = "Django Email Test"
    message = "Hello Yvonne, this is a test email from your Django app!"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ["ndunguyvonne10@gmail.com"]

    send_mail(subject, message, from_email, recipient_list)

    return HttpResponse("Email sent successfully!")
        

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('task-list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})