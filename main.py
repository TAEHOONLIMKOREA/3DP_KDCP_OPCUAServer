import asyncio

from opcua import server


test = server.StartServer()

asyncio.run(test)
