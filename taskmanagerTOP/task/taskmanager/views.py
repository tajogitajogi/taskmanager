from django.shortcuts import render
from .models import Task
# Create your views here.
def index(request):
    task = Task.objects.all()

    for el in task:
        date=el.date
        time=el.time
        w=date.split('.')
        mod=int(time)//8 
        w[0]=str(int(w[0])+mod)
        el.stop='.'.join(w)
    return render(request,'index.html', {'task':task})


    

 