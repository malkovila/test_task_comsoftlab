import json
from channels.generic.websocket import AsyncWebsocketConsumer

class EmailProgressConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        self.progress = 0

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        if data['action'] == 'start_import':
            for i in range(100):
                self.progress += 1
                await self.send(json.dumps({'progress': self.progress}))
                await asyncio.sleep(0.1)
