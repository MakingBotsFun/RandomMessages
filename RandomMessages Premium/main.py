import discord
from discord.ext import commands
import asyncio
# If error, pip install discord-py-slash-command
import discord_slash
from discord_slash import SlashCommand
client = discord.Client()

import random
import os
import keep_alive
keep_alive.keep_alive()

bot = commands.Bot(command_prefix='rmp!')
slash = SlashCommand(bot, sync_commands=True)

@slash.slash(description="Premium flex!")
@commands.has_any_role(930220504894279720, 926228047022141461)
async def premiumflex(ctx):
  pfl = ['failed', 'got successful!', 'showed a mega flex']
  embed = discord.Embed(title='Premium Flex', description='{0} has {1}'.format(ctx.author.mention, random.choice(pfl)), color=discord.Color.gold())
  await ctx.send(embed=embed)


@slash.slash(description="Pro Motivation quote randomly!")
@commands.has_role(930220504894279720)
async def promotivation(ctx):
  promotivationl = ['To obtain desire, hard work has to be done. - Anonymous', 'There will be downhills. But there are surely uphills too. - Anonymous', 'A hill of desire has to be climbed manually. - Anonymous', 'Being wrong is good when you learn from it. - Anonymous', 'Being right is not always good - sometimes being wrong is a learning point. - Anonymous']
  embed = discord.Embed(title='Pro Motivation', description=random.choice(promotivationl), color=discord.Color.green())
  await ctx.send(embed=embed)


@slash.slash(description="Credits for the bot")
@commands.has_any_role(930220504894279720, 926228047022141461)
async def credits(ctx):
  embed = discord.Embed(title='Credits', description='If <@920419311691116544> is in a server, type rm!credits in that server for most of the credits of this bot too possibly.', color=discord.Color.green())
  await ctx.send(embed=embed)


@slash.slash(description="Are you a pro as a premium?")
@commands.has_any_role(930220504894279720, 926228047022141461)
async def premiumpro(ctx):
  pprorl = ['Yes', 'No', 'N/A', 'Maybe!']
  embed = discord.Embed(title='Are you a premium pro?', description=random.choice(pprorl), color=discord.Color.gold())
  await ctx.send(embed=embed)

@slash.slash(description="Are u sus?")
@commands.has_any_role(930220504894279720, 926228047022141461)
async def suscheck(ctx):
  susl = ["very sus!", "sus.", "not sus."]
  embed = discord.Embed(title='Sus Checker', description="You are {}".format(random.choice(susl)), color=discord.Color.green())
  embed.set_footer(text='This commands idea was not by Chai_rbf#9987 or any of the developers for now')
  await ctx.send(embed=embed)
from discord_slash.utils import manage_components
from discord_slash.model import ButtonStyle
from discord_slash.utils.manage_commands import create_choice, create_option
@slash.slash(description="Bot support server!")
@commands.cooldown(1,50,commands.BucketType.user)
async def supportserver(ctx):
  buttons= [
    manage_components.create_button(
      style=ButtonStyle.URL,
      label="Support Server", url="https://discord.gg/qgZpzUdGgg"
    )
  ]
  action_row = manage_components.create_actionrow(*buttons)
  await ctx.send("Hey! Please click the button below.", components=[action_row])
  
@slash.slash(description="Common errors!")
@commands.has_any_role(930220504894279720, 926228047022141461)
async def commonerrors(ctx):
  embed = discord.Embed(title='Common Errors', description='Common errors you might see while using the bot.', color=discord.Color.gold())
  embed.add_field(name='Invalid Application Command (credit: Discord)', value='If you get this, it means the command might be on cooldown OR the command has a error.')
  embed.add_field(name='The application did not respond (credit: Discord)', value='This may also be due to cooldown of a command. If not, it could be a bg which you can report in the support server for now.')
  await ctx.send(embed=embed)

@slash.slash(description="Only for Chai_rbf#9987: StatusChanging")
@commands.has_any_role(920449565633687612)
async def devstatuschange(ctx):
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="premium commands"))
  embed = discord.Embed(title='Status Change - DO NOT USE', description='Accepted, {}!'.format(ctx.author.mention), color=discord.Color.green())    
  embed = discord.Embed(title='Status Change - DO NOT USE', description='Accepted, {}!'.format(ctx.author.mention), color=discord.Color.green())
  await ctx.send(embed=embed)

@bot.command()
@commands.cooldown(1,60,commands.BucketType.user)
@commands.has_any_role(930220504894279720, 926228047022141461)
async def hackbot(ctx):
  message = await ctx.send('0% - Trojan injection started...')
  await asyncio.sleep(4)
  await message.edit(content='5% - Trojan injected')
  await asyncio.sleep(5)
  await message.edit(content='20% - Logging token...')
  await asyncio.sleep(5)
  await message.edit(content='25% - Logged Token')
  await asyncio.sleep(5)
  await message.edit(content='50% - Bot files taken')
  await asyncio.sleep(3)
  await message.edit(content='100% - Bot hosting deleted')
  await asyncio.sleep(2)
  await message.edit(content='The hack by {} has got successful!'.format(ctx.author.mention))

bot.run('TOKEN_HERE')
