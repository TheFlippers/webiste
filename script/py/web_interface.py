from controller import Controller

import asyncio
import json
import websockets

class WebInterface(Controller):
    def __init__(self, key_interface={'Left': ('w', 's'), 'Right': ('o', 'l')}, start_key='r'):
        super()
        self.clients = {'Left': None, 'Right': None}
        self.keys = {'Left': None, 'Right': None, 'start': False}
        self.key_interface = key_interface
        self.start_key = start_key

    def server_run_forever(self, domain=None, port=6789):
        start_server = websockets.serve(self.client_handler, domain, port)

        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()

    def read(self):
        output = []
        
        if self.keys['start'] is True:
            output.append(self.start_key)

        for key in self.keys.keys():
            if self.keys[key] == 'up':
                output.append(self.key_interface[key][0])
            elif self.keys[key] == 'down':
                output.append(self.key_interface[key][1])
        return output

    async def register_client(self, websocket):
        for client in self.clients.keys():
            if self.clients[client] is None:
                self.clients[client] = websocket
                message = json.dumps({'player': client})
                await websocket.send(message)
                return client

        message = json.dumps({'player': 'Not a'})
        await websocket.send(message)
        return None

    async def unregister_client(self, websocket):
        for client in self.clients.keys():
            if self.clients[client] is websocket:
                self.clients[client] = None
                break

    async def client_handler(self, websocket, path):
        # Register new web socket as player
        player = await self.register_client(websocket)

        # Handle overflow players
        if not player:
            return

        # Handle web socket connection
        try: 
            # Parse each message for button presses and releases
            async for message in websocket:
                data = json.loads(message)
                if data['action'] == 'none':
                    self.keys[player] = None
                elif data['action'] == 'start':
                    self.keys['start'] = True
                else:
                    self.keys[player] = data['action']
        finally:
            # Remove player on disconnect
            await self.unregister_client(websocket)

if __name__ == '__main__':
    controller = WebInterface()
    controller.server_run_forever()
