import random
import discord
import music, role
from discord.ext import commands
#Add token here
TOKEN = ''

client = commands.Bot(command_prefix=".!")

cogs = [music, role]

for i in range(len(cogs)):
    cogs[i].setup(client)

@client.event
async def on_ready():
        print('We have logged in as {0.user}' .format(client))

        
client.run(TOKEN)