from django.db import models
from dateFunc import getDate



class Todo(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField(max_length=500,blank=True)
    isFinished=models.BooleanField(default=True)
    date=models.DateTimeField(default=getDate())

