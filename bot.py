import discord
from config import TOKEN
from commands.messages_handler import handle_message
from events.presence_handler import handle_presence_update

intents = discord.Intents.default()
intents.message_content = True
intents.presences = True
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    await handle_message(message)

@client.event
async def on_presence_update(before, after):
    await handle_presence_update(before, after)

client.run(TOKEN)