import discord
import os 

from discord.ext import commands

bot = commands.Bot(command_prefix="__")

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")

@bot.event
async def on_ready():
    print("Bot is not ready!")

bot.run("ODg0MzYxODU5MjYyNzIyMDU5.YTXYKQ.KeUnVtm5YvM4X-yZA5HHWtUzepo")