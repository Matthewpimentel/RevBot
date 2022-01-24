import discord
import music, role, secret
from discord.ext import commands



client = commands.Bot(command_prefix=".!")

cogs = [music, role]

for i in range(len(cogs)):
    cogs[i].setup(client)

@client.event
async def on_ready():
        print('We have logged in as {0.user}' .format(client))

        
client.run(secret.TOKEN)