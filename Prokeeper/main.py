import nextcord
import random
import nextcord
from nextcord import *
from nextcord.abc import GuildChannel
from nextcord.ext import commands
from config import *
import config
import keep_alive
keep_alive.keep_alive()

client = commands.Bot(command_prefix='pk!')


@client.event
async def on_ready():
  await client.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.watching, name=f"the raiders"))

@client.listen()
async def on_message(message):
  if message.content.startswith("@everyone"):
    await message.delete()
    member = message.author
    embed = nextcord.Embed(title=f"Banned from {message.guild.name}", description=f"You have been banned from {message.guild.name} for raiding. This is a automatic ban.", color=nextcord.Color.red())
    await member.send(embed=embed)
    await member.ban()
    
  if message.content.startswith("@here"):
    await message.delete()
    member = message.author
    embed = nextcord.Embed(title=f"Banned from {message.guild.name}", description=f"You have been banned from {message.guild.name} for raiding. This is a automatic ban.", color=nextcord.Color.red())
    await member.send(embed=embed)
    await member.ban()
  else:
    if len(message.mentions) > 7:
     await message.delete()
     embed = nextcord.Embed(title=f"Banned from {message.guild.name}", description=f"You have been banned from {message.guild.name} for raiding. This is a automatic ban.", color=nextcord.Color.red())
     member = message.author
     await member.send(embed=embed)
     await member.ban()
    

@client.command()
@commands.has_role(927770913372504074)
@commands.cooldown(1,604800,commands.BucketType.user)
async def ban(ctx, member : nextcord.Member, *, reason='MBF DISCORD MODERATION ACTION'):
  await member.send(f"You have been banned from {ctx.guild.name} per moderator request. In case you get unbanned, here is the link to the server: https://discord.gg/qgZpzUdGgg")
  await ctx.guild.ban(member, reason=reason)
  embed = nextcord.Embed(description='Person has been banned.', color=nextcord.Color.red())
  await ctx.send(embed=embed)

@client.command()
@commands.has_role(927770913372504074)
@commands.cooldown(1,259200,commands.BucketType.user)
async def kick(ctx, member : nextcord.Member, *, arg, reason='MBF DISCORD MODERATION ACTION'):
  await member.send(f'You have been kicked from MBFs discord server for "{arg}"" from a moderator. You can rejoin from here for now: https://discord.gg/qgZpzUdGgg')
  await ctx.guild.kick(member, reason=reason)

@client.command()
async def credits(ctx):
  await ctx.send('Credit: https://discordpy.readthedocs.io/ for the helping with bot development, https://discord.com/channels/336642139381301249/381965515721146390/931324486123388938 for helping with a ban command, google for helping with the time for the ban command in seconds, and https://www.youtube.com/watch?v=THj99FuPJmI for helping with the kick and ban, and https://stackoverflow.com/questions/49352368/discord-py-delete-author-message-after-executing-command for helping with deleting messages.')

@client.slash_command()
@commands.has_role(927770913372504074)
@commands.cooldown(1,500,commands.BucketType.user)
async def moderationnotice(interaction : nextcord.Interaction):
  embed = nextcord.Embed(title='Moderation Notice', description='A discord moderation department member of MBF has gave a moderation notice to tell people to follow RandomMessages rules.', color=nextcord.Color.red())
  await interaction.send(embed=embed)

@client.command()
@commands.has_role(920449615118090270)
async def dm(ctx, user : nextcord.User, *, arg):
  await user.send({arg})

@client.command()
@commands.has_role(920449615118090270)
async def lockdown(ctx):
  channel1 = await client.fetch_channel(941705411990544434)
  channel2 = await client.fetch_channel(939160384806461440)
  channel3 = await client.fetch_channel(920450767234674698)
  channel4 = await client.fetch_channel(920449812812410891)
  await channel1.set_permissions(ctx.guild.default_role, read_messages = True, send_messages=False)
  await channel2.set_permissions(ctx.guild.default_role, read_messages = True, send_messages=False)
  await channel3.set_permissions(ctx.guild.default_role, read_messages = True, send_messages=False)
  await channel4.set_permissions(ctx.guild.default_role, read_messages = True, send_messages=False)
  await ctx.send("Successfully locked down most of the server.")

@client.command()
@commands.has_role(920449615118090270)
async def unlockdown(ctx):
  channel1 = await client.fetch_channel(941705411990544434)
  channel2 = await client.fetch_channel(939160384806461440)
  channel3 = await client.fetch_channel(920450767234674698)
  channel4 = await client.fetch_channel(920449812812410891)
  await channel1.set_permissions(ctx.guild.default_role, read_messages = True, send_messages=True)
  await channel2.set_permissions(ctx.guild.default_role, read_messages = True, send_messages=True)
  await channel3.set_permissions(ctx.guild.default_role, read_messages = True, send_messages=True)
  await channel4.set_permissions(ctx.guild.default_role, read_messages = True, send_messages=True)
  await ctx.send("Successfully unlocked down most of the server.")


@client.command()
async def aboutme(ctx):
  embed = nextcord.Embed(title="👋Hey there!", description="I am ProKeeper, I am a AI bot which is for moderation of Making Bots Fun. I help moderators of this server do their job easier.", color=nextcord.Color.green())
  await ctx.send(embed=embed)
  

client.run('TOKEN_HERE')
