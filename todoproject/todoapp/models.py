from django.db import models
from datetime import datetime



class Todo(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField(max_length=500,blank=True)
    isFinished=models.BooleanField(default=False)
    date=models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.title

