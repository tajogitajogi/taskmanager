from django.shortcuts import render,get_object_or_404,redirect
from datetime import timedelta, datetime
from .models import Task


def index(request):
    task = Task.objects.order_by('start')
    for el in task:
        start=el.start
        time=el.time
        el.stop=timedelta(int(time)//8)+start
    return render(request,'taskmanager/main.html', {'task':task})


def delete(request,pk):
    obj=get_object_or_404(Task,pk=pk)
    obj.delete()
    return render(request,'taskmanager/main.html',{'obj':obj}) and redirect('main')