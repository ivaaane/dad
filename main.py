import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

def hidad(message):
    prefixes = ("i am", "i'm", "im")
    msg = message.content.lower()
    for i in prefixes:
        if msg.startswith(i):
            return message.content[len(i):]
    return None

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    await bot.tree.sync()

@bot.event
async def on_message(message):
    if message.author == bot.user: return
    hi = hidad(message)
    if hi:
        await message.channel.send(f"Hi{hi.title()}, I'm Dad!")
    await bot.process_commands(message)

bot.run(TOKEN)
