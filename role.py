import discord
from discord.ext import commands

class role(commands.Cog):
    def __init__(self, client):
        self.client = client
        
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

        @client.event
        async def on_raw_reaction_remove(payload):
            messageID = 934155255925587978
            if messageID == payload.message_id:
                guild = await(client.fetch_guild(payload.guild_id))
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
                member = await(guild.fetch_member(payload.user_id))
                if member is not None:
                    await member.remove_roles(role)
        
def setup(client):
    client.add_cog(role(client))