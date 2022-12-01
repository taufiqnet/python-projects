from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth import login

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View

from .models import *
from .forms import *

class CustomLoginView(LoginView):
   template_name = 'base/login.html'
   fields = '__all__'
   redirect_authenticated_user = True
   
   def get_success_url(self):
      return reverse_lazy('tasks')

def task(request):
   tasks = Task.objects.all()
   
   form = TaskForm()
   
   if request.method == 'POST':
      form = TaskForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect('/tasks')
      
   context = {'tasks':tasks, 'form':form}
   return render(request, 'tasks/list.html', context)

def updateTask(request, pk):
   task = Task.objects.get(id=pk)
   
   form = TaskForm(instance=task)
   
   if request.method == 'POST':
      form = TaskForm(request.POST, instance=task)
      if form.is_valid():
         form.save()
         return redirect('/tasks')
      
   context = {'form':form}
   return render(request, 'tasks/update_task.html', context)

def deleteTask(request, pk):
   item = Task.objects.get(id=pk)
   
   if request.method == 'POST':
      item.delete()
      return redirect('/tasks')
   
   context = {'item':item}
   return render(request, 'tasks/delete.html', context)
