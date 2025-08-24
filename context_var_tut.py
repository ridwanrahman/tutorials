import asyncio
import contextvars


async def handle_request(reader, writer):
    pass

async def runner():
    server = await asyncio.start_server(
        handle_request, '127.0.0.1:8081'
    )
    async with server:
        await server.serve_forever()

def main():
    asyncio.run(runner())

if __name__ =="__main__":
    main()
