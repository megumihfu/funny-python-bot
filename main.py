import os
import asyncio
from flask import Flask
from threading import Thread

from discord_bot import discord_client
from stoat_bot import stoat_client

app = Flask('')

@app.route('/')
def home():
    return "Your Bot is online :)"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

def run_stoat_bot():
    token = os.environ.get("BOT_TOKEN")

    if token: 
        stoat_client.run(token)
    else:
        print("No stoat token configured")

async def run_discord_bot():
    token = os.environ.get("DISCORD_TOKEN")

    if token: 
        await discord_client.start(token)
    else:
        print("No discord token configured")

if __name__ == "__main__":
    keep_alive()

    try:
        stoat_thread = Thread(target=run_stoat_bot)
        stoat_thread.start()

        asyncio.run(run_discord_bot())
    except KeyboardInterrupt:
        print("Bots were stopped")