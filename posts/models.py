from django.db import models
from datetime import datetime

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=1000000)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title
    
class Task(models.Model):
    title =  models.CharField(max_length=400)
    complete = models.BooleanField(default=False)
    #body = models.CharField(max_length=1000000)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title