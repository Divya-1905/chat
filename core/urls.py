from unicodedata import name
from core.form import signup
from.views import*
from django.urls import path
urlpatterns = [
    path('chat',chat,name='chatview'),
    path('<str:room_name>/',chat_room,name='chatroom-view'),
    path('accounts/signup/',signupview, name='signup'),
    path('accounts/login/',loginview,name='login'),
    path('accounts/message',message,name='message')
    
   
]