import random
from api import tasks

import asyncio
from channels.consumer import AsyncConsumer


class SampleConsumer(AsyncConsumer):

    def __init__(self):
        self.connected = True

    async def websocket_connect(self, event):
        await self.send({
            "type": "websocket.accept"
        })

        while self.connected:
            await asyncio.sleep(0.1)

            await self.send({
                'type': 'websocket.send',
                'text': str(tasks.add.delay(random.randint(1, 10), random.randint(1, 10)).get())
            })

    async def websocket_receive(self, event):
        print("receive", event)

    async def websocket_disconnect(self, event):
        print("disconnected", event)
        self.connected = False
