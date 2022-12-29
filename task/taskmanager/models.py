from django.db import models

class Task(models.Model):
    title = "Task"
    task= models.CharField('task',max_length=30)
    date= models.CharField('Начальная дата',max_length=10)
    time= models.CharField('Время',max_length=2)
    
    
    def __str__(self):
        return self.title


