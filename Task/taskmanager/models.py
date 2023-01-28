from django.db import models

class Task(models.Model):
    title = "Task"
    task= models.CharField('task',max_length=30)
    start= models.DateField('Начальная дата')
    time= models.CharField('Время',max_length=3)
    stop=0

    
    def __str__(self):
        return self.task


