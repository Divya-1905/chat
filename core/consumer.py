import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import room
import channels
from django.http import HttpResponse
from channels.db import database_sync_to_async



class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
         self.room = self.scope['url_route']['kwargs']['room_name']
                                                                    #it mention the key and value its taken  
         self.roomGroupName = 'chatroom-%s' % self.room 
                                                                       
         self.user=await channels.auth.get_user(self.scope)
         print(self.scope)
         print(self.user)
         roomcheck = await self.get_room()
                                                                  # this query  object crete
        #  print(self.scope, 'scope')
        #  print(self.scope['url_route'])
         if roomcheck:
             await self.channel_layer.group_add(
			 self.roomGroupName,
			 self.channel_name,)
             await self.accept()
         else:
            return HttpResponse('YOUR  NOT ADMIN')   
                                                                   #data base room save function
    @database_sync_to_async    
    def get_room(self):
        data = room.objects.filter(room=self.room,user=self.user.id)
        if data.exists():
            return True
        else :
             return False
    async def disconnect(self , close_code):
        await self.channel_layer.group_discard(
			self.roomGroupName ,
			self.channel_layer
		)
    async def receive(self, text_data):
                 text_data_json = json.loads(text_data)
                 message = text_data_json["message"]
                 
                 username = text_data_json['user']
                 print(text_data_json)
                
                 await self.channel_layer.group_send(
                     self.roomGroupName,{
                         "type" : "sendMessage" ,
				         "message" : message ,
                         "username": username,
				       
			})
               
    async def sendMessage(self , event) :
        message = event["message"]
        username = event['username']
       
        await self.send(text_data = json.dumps({"message":message,'username':username}))
