from log_events import *
from koya import *
import discord

username = "skppy7#1176"

client = discord.Client()

@client.event
async def on_ready():
    printimed(f"Bot routine started succesfully as {client.user}")

@client.event
async def on_message(message):

    if message.author.__str__() == "Koya#1050":
        analize_msg(message.content.__str__())

    elif message.author.__str__() == username:
        if message.content.startswith('/stop'):
            await message.channel.send('Routine is closing...')
            await client.close()
            printimed("Bot routine closed!")
    else:
        return
