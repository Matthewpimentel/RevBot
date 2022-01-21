import random
import discord


    
        
intents = discord.Intents.default()
intents.members = True

#add your token
TOKEN = ''
client = discord.Client()

@client.event
async def on_ready():
        print('We have logged in as {0.user}' .format(client))

#React role add (add the message id and emoji/roles to fit your needs)
@client.event
async def on_raw_reaction_add(payload):
    messageID = 934155255925587978
    if messageID == payload.message_id:
        member = payload.member
        guild = member.guild
        
        emoji = payload.emoji.name
        if emoji == '🕵️‍♂️':
            role = discord.utils.get(guild.roles, name="Detective")
        elif emoji == '🔫':
            role = discord.utils.get(guild.roles, name="Headshot Machine")
        elif emoji == '🏎️':
            role = discord.utils.get(guild.roles, name="Boost Stealer")
        elif emoji == '👻':
            role = discord.utils.get(guild.roles, name="Ghostbuster")
        elif emoji == '🎲':
            role = discord.utils.get(guild.roles, name="Table Flipper")
        elif emoji == '🇱':
            role = discord.utils.get(guild.roles, name="Lost Ark")

        await member.add_roles(role)
        
client.run(TOKEN)