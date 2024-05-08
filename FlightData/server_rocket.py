"""
This script is used to constatly translate CSV data to a server.
One row at a time, with convertion to JSON. When file ends, it starts again.
"""


from aiohttp import web
import aiohttp
import asyncio
import csv
import json
from urllib.parse import urlparse


class ServerRocket:
    def __init__(self) -> None:
        self.csv_path = None
        self.post_url = None
        self.current_row = None
        self.app = None
        self.runner = None

    def update_vars(self, csv_path: str, post_url: str) -> None:
        self.csv_path = csv_path
        self.post_url = post_url
        
    async def handler(self, request):
        if self.current_row:
            return web.Response(text=f"{','.join(map(str, self.current_row))}")
        else:
            return web.Response(text="")
        
    async def start_server(self):
        url_components = urlparse(self.post_url)
        host = url_components.hostname
        port = url_components.port

        self.app = web.Application()
        self.app.add_routes([web.get('/', self.handler)])
        self.runner = web.AppRunner(self.app)
        await self.runner.setup()
        site = web.TCPSite(self.runner, host, port)
        await site.start()

    async def send_row(self, row):
        async with aiohttp.ClientSession() as session:
            async with session.post(self.post_url, data=','.join(map(str, row))) as response:
                self.current_row = row
                if response.status != 200:
                    print(f"Failed to send row: {','.join(map(str, row))}")

    async def run(self):
        while True:
            with open(self.csv_path, 'r') as file:
                csv_reader = csv.reader(file)
                for csv_row in csv_reader:
                    json_row = json.dumps(csv_row)
                    await self.send_row(json_row)
                    await asyncio.sleep(50 / 1000)  # First is delay in ms


if __name__ == "__main__":
    server_rocket = ServerRocket()
    server_rocket.update_vars(
        csv_path="FlightData\simulations\sim1-v1.csv",
        post_url="http://localhost:8080"
    )
    
    asyncio.run(server_rocket.start_server())
    asyncio.run(server_rocket.run())
