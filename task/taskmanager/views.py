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
        if (int(w[1]) == 1 or int(w[1]) == 3 or int(w[1]) == 5 or int(w[1]) == 7 or int(w[1]) == 8 or int(w[1]) == 10 or  int(w[1]) == 12) and (int(w[0])>31):
            w[1]='0'+str(int(w[1])+1)
            w[0]=str(int(w[0])-32)
        if (int(w[1]) == 4 or int(w[1]) == 6 or int(w[1]) == 9 or int(w[1]) == 11) and (int(w[0])>30):
            w[1]='0'+str(int(w[1])+1)
            w[0]=str(int(w[0])-31)
        if int(w[1]) == 2 and (int(w[0])>28):
            w[1]='0'+str(int(w[1])+1)
            w[0]=str(int(w[0])-29)
        if int(w[1])>12:
            w[1]='1'
            w[2]=str(int(w[2])+1)
        if int(w[0]) == 0:
            w[0]='1'
        el.stop='.'.join(w)
    return render(request,'index.html', {'task':task})


    

 