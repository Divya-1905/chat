import email
from email.message import Message
import re
from urllib import request, response
from django.http import JsonResponse
from django.shortcuts import render,redirect
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from django.http import Http404
from core.form import signup,loginform,messageform,createform
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate,login,logout
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User 
from .models import room
from django.http import HttpResponse    

def chat(request):
    print(request.user.username)
    form = createform()
    if request.method =='POST':
        data =request.POST.get('room')
                                                                 #database save function, exists= check a true or false function 
        if room.objects.filter(room=data).exists():
            return HttpResponse('<p>already exists</p>')   
        else:                                                 
           user = request.user                                  
                                                                 #its  create a function it mention a room model - create function
           room.objects.create(room=data,user=user)
           return render(request,'core/index.html',{'form':form})
    return render(request,'core/index.html',{'form':form})
    

def chat_room(request,room_name):
    return render(request,'core/chat.html',{'roomname':room_name,'user':request.user.username})
def  signupview(request):
    form = signup()
                                        
    if request.method=='POST':
        print('hai')
        data = signup(request.POST)
    
        if  data.is_valid():
           print('hai')
           data.save()
        else:
            print(form.errors)   
       
                                                                                   # data base saved function    
    return render(request,'core/signup.html',{'form':form,})
def loginview(request):
    form = loginform()
    if request.method=='POST': 
        user1 = request.POST.get('username')
        password   = request.POST.get('password')
        user = authenticate(request,username=user1,password=password)
        print(user)
        if user:
            login(request,user)
            return redirect('room')  
    return render(request,'core/login.html',{'form':form})

   





















# def message(request):
#     form = messageform()
#     print('hai')
#     if request.method =='POST':
#         print('hai')
#         message = request.POST.get('message')
#         if message.is_valid():
#            message.save()
#            return redirect('message')
#     return render(request,'core/message.html',{'form':form})
    
    
    
    
    
    
    
    # if request.method=='POST':
    #     print('hai')
    #     message = request.POST.get('message') 
    #     if message.is_vaild():
    #         message.save()
    #         return redirect('message')
    #     print(request.POST.data) 
    # return render(request,'core/message.html',{'form':form,})  