import discord
from discord import Client, Member
import asyncio
import pathlib




client: Client = discord.Client()




@client.event
async def on_ready():
    print("\aWir sind eingeloggt als User {}".format(client.user.name))
    client.loop.create_task(status_task())

    
async def status_task():
    while True:
        await client.change_presence(activity=discord.Game("Für hilfe 'hilfe"), status=discord.Status.online)
        await asyncio.sleep(2)
                



client.run(pathlib.Path("Zugangsdaten/StatusBot.credentials.txt").read_text())
