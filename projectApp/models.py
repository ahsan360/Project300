from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.utils import timezone
# Create your models here.

 
class Add(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.TextField(max_length=5000)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return redirect('posts')   

class Hello(models.Model):
   name = models.CharField(max_length=100)
   image = models.ImageField(null=True,blank=True,upload_to="images/")
   post =   models.ForeignKey(Add,related_name="comments",on_delete=models.CASCADE,null=True)
   body = models.TextField()
   date_added = models.DateTimeField(auto_now_add=True)

   def __str__(self):
        return self.body


