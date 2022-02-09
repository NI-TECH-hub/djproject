from ast import Delete
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import TODO
from .forms import TodoForm

# Create your views here.

def homepage(request):
    # print(request)
    data = TODO.objects.all() #select * from todo
    form = TodoForm()
    # print(form)

    context = {
        'data':data,
        'form':form
    }

    return render(request,'base.html',context)

def addtodo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/')

def Delete_Task(request,id):
    if request.method=="POST":
        item = TODO.objects.get(pk=id)
        item.delete()
        return HttpResponseRedirect('/')
    return HttpResponseRedirect('/')