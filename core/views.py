import email
from urllib import request, response
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from django.http import Http404
from core.form import signup,login
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate,login,logout
from rest_framework.authtoken.models import Token

def chat(request):
    return render(request,'core/index.html')
def chat_room(request,room_name):
    return render(request,'core/chat.html',{'roomname':room_name})
def  signupview(request):
    form = signup()
    if request.method=='POST':
        
        # form1= signup (request.data)
        print(request.POST.data)
        # if form1.is_valid():
            # form1.save()
    return render(request,'core/signup.html',{'form':form})
def loginview(request):
    form = login()
    if request.method=='POST':
        user = request.POST.get('username')
        email   = request.POST.get('emailaddress')        
        print(request.POST.data)
        return render(request,'core/login.html',{'form':form,'user':user,'email':email})
def message(request):
    form = message() 
    if request.method=='POST':
        message = request.POST.get('message')
        print(request.POST.data) 
        return render(request,'core/message.html',{'form':form,'message':message})  