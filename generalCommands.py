# import discord
# from discord.ext import commands

# class generalCommands(commands.Cog):
#     def __init__(self, client):
#         self.client = client
        
#         @client.command(pass_context = True)
#         @commands.has_role("Admin" or "Owner")
#         async def muteall(ctx):
#             if ctx.author.voice:
#                 channel = ctx.author.voice.channel
#                 members = channel.voice_members
#                 mutedRole = discord.utils.get(guild.roles, name="Muted")
                

#             for member in members:
                
            
        
# def setup(client):
#     client.add_cog(generalCommands(client))