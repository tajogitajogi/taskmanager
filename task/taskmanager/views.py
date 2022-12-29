from django.shortcuts import render
from .models import Task
# Create your views here.
def index(request):
    task = Task.objects.all()
    stopstart=[]
    stoptime=[]
    stop=[]
    for el in task:
        stopstart.append(el.date)
        stoptime.append(el.time)
    for i in range(0, len(stopstart)):
        w=stopstart[i].split('.')
        mod=int(stoptime[i])//8 
        w[0]=str(int(w[0])+mod)
        stop.append('.'.join(w))

        
    return render(request,'index.html', {'task':task, 'stop':stop})


 