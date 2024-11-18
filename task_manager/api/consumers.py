import json
from channels.generic.websocket import AsyncWebsocketConsumer


class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope['user']
        self.group_name = f"user_{self.user.id}_notifications"
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()
        print(f"Connexion WebSocket acceptée pour l'utilisateur {self.user.username}")

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )
        print(f"Déconnexion WebSocket pour l'utilisateur {self.user.username}")

    async def send_notification(self, event):
        print(f"Notification reçue : {event['message']}")
        await self.send(text_data=json.dumps(event["message"]))
