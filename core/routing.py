from email.mime import application
from importlib.resources import path
from channels.routing import ProtocolTypeRouter,URLRouter
from django.urls import path
from .consumer import ChatConsumer
websocket_urlspatterns = [
    path('ws/asgi/<str:room_name>/',ChatConsumer.as_asgi()),
]
