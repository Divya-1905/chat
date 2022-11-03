from distutils import core
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
class messagemodel(models.Model):
    message = models.TextField(max_length=100000)
    def  __str__(self):
       return self.message
class chatroom(models.Model):
    roomname = models.CharField(max_length=100)  
class room(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)   