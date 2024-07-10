import discord
import asyncio
import requests
import json
from tokens import lostark_token, discord_token
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

headers = {
    'accept' : 'application/json',
    'authorization' : lostark_token
}


@bot.event
async def on_rady():
    print(bot.user)
    
@bot.command()
async def ping(ctx):
    await ctx.send(f'pong! {round(round(bot.latency, 4)*1000)}ms')

bot.run(discord_token)