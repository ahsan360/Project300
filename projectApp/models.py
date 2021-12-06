from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import redirect
# Create your models here.

 
class Add(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.TextField(max_length=5000)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return redirect('posts')   
 