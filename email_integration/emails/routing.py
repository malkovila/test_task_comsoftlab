from django.urls import path
from .consumers import EmailProgressConsumer

websocket_urlpatterns = [
    path('ws/progress/', EmailProgressConsumer.as_asgi()),
]
