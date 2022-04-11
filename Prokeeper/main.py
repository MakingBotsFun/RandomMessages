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

@client.command()
@commands.has_role(927770913372504074)
@commands.cooldown(1,604800,commands.BucketType.user)
async def ban(ctx, member : nextcord.Member, *, reason='MBF DISCORD MODERATION ACTION'):
  await member.send('You have been banned from MBF per moderator request. In case you get unbanned, here is the link to the support server: https://discord.gg/qgZpzUdGgg')
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

@client.command()
@commands.has_role(927770913372504074)
@commands.cooldown(1,500,commands.BucketType.user)
async def moderationnotice(ctx):
  embed = nextcord.Embed(title='Moderation Notice', description='A discord moderation department member of MBF has gave a moderation notice to tell people to follow RandomMessages rules.', color=nextcord.Color.red())
  await ctx.send(embed=embed)

@client.command()
@commands.has_role(920449615118090270)
async def dm(ctx, user : nextcord.User, *, arg):
  await user.send({arg})


client.run('TOKEN_HERE')
