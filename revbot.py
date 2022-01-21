import random
import discord


TOKEN = 'OTM0MTM0MTcwODE5NjQ1NDcw.YerqPQ.W4tJS1prkXl79kCM-lUCgP78zJg'
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}' .format(client))
    
client.run(TOKEN)