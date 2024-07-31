import discord
import asyncio
import requests
import json
from tokens import lostark_token, discord_token
from discord.ext import commands

intents = discord.Intents.default()
client = discord.Client(intents=intents)

headers = {
    'accept': 'application/json',
    'authorization': lostark_token
}

# 사용자가 입력한 캐릭터 이름을 기반으로 URL 생성
def create_url(character_name):
    base_url = "https://developer-lostark.game.onstove.com/armories/characters/{}/profiles"
    return base_url.format(character_name)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!캐릭터 '):
        character_name = message.content[len('!캐릭터 '):].strip()
        url = create_url(character_name)
        
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            jsonObject = response.json()
            
            embed = discord.Embed(title="Lost Ark 캐릭터 정보", color=discord.Color.blue())
            embed.add_field(name="서버 이름", value=jsonObject.get("ServerName"), inline=True)
            embed.add_field(name="캐릭터 이름", value=jsonObject.get("CharacterName"), inline=True)
            embed.add_field(name="클래스 이름", value=jsonObject.get("CharacterClassName"), inline=True)
            embed.add_field(name="아이템 최대 레벨", value=jsonObject.get("ItemMaxLevel"), inline=True)
            embed.set_thumbnail(url=jsonObject.get("CharacterImage"))
            
            await message.channel.send(embed=embed)
        else:
            await message.channel.send(f"오류: {response.status_code} {response.text}")

client.run(discord_token)
