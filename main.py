from bot import Bot
import asyncio
import aiohttp
import os

URL = "https://rolling-nikkie-drxyhacker12-3c8942d4.koyeb.app/"

async def ping():
    async with aiohttp.ClientSession() as session:
        while True:
            try:
                async with session.get(URL) as response:
                    print(f"Pinged server, status: {response.status}")
            except Exception as e:
                print(f"Ping error: {e}")
            await asyncio.sleep(600)  # 10 minutes

def main():
    try:
        bot = Bot()  # Create an instance of the Bot class
        loop = asyncio.get_event_loop()
        loop.create_task(ping())
        bot.run()  # Run the bot instance
    except Exception as e:
        print(f"Main error: {e}")
        # If the bot crashes, exit with error code so Heroku can restart it
        os._exit(1)

if __name__ == "__main__":
    main()
