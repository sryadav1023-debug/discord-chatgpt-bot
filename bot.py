import os
import discord
from discord.ext import commands

TOKEN = os.getenv("TOKEN")  # Railway pe variable set hoga

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Bot logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send("Hello! I'm alive ✅")

bot.run(TOKEN)
