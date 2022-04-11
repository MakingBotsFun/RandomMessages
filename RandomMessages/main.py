# MODIFIED VERSION OF ORIGINAL CODE OF 2/16/2022
# IT IS SUGGESTED YOU USE REPL.IT FOR THIS
# SOME THINGS MAY BE INCORRECT, MAKING BOTS FUN WILL NOT BE LIABLE FOR THIS NOR WILL THE FOUNDER CHAI_RBF BE

import discord
import random
import os
import keep_alive
from discord.ext import commands
from discord_slash.utils import manage_components
from discord_slash.model import ButtonStyle
keep_alive.keep_alive()
client = discord.Client()
bot = commands.Bot(command_prefix='rm!')
@bot.event
async def on_ready():
       print('We have logged in as {0.user}'.format(bot))
    
@bot.event
async def on_message(message):
    if message.author == bot.user:
      return

@bot.event
async def on_message(message):
   await bot.process_commands(message)
   return


@bot.command()
@commands.cooldown(2,30,commands.BucketType.user)
async def norrandom(ctx):
  norlist = ['Nickel', 'Dime']
  embed = discord.Embed(title='Nickel Or Dime', description=random.choice(norlist),color=discord.Color.green())
  embed.set_footer(text='The thing you get in the embed does not have any real value of money, this is just a fun command interactive.')
  await ctx.send(embed=embed)

   
@bot.command()
@commands.cooldown(1,500,commands.BucketType.user)
async def suggestions(ctx):
   await ctx.send('Suggest here: https://discord.gg/qgZpzUdGgg')

@bot.command()
@commands.cooldown(2,500,commands.BucketType.user)
async def termsofservice(ctx):
  buttons =[
    manage_components.create_button(
      style=ButtonStyle.URL,
      label="Terms Of Service",
      url='https://sites.google.com/view/randommessages/randommessages-tos'

    )
  ]
  embed=discord.Embed(title='Terms Of Service', description='Please click the button below.', color=discord.Color.red())
  action_row = manage_components.create_actionrow(*buttons)
  await ctx.send(embed=embed, components=[action_row])

@bot.command()
@commands.cooldown(2,500,commands.BucketType.user)
async def privacypolicy(ctx):
  buttons =[
    manage_components.create_button(
      style=ButtonStyle.URL,
      label="Privacy Policy",
      url='https://sites.google.com/view/randommessages/randommessages-privacy-policy'

    )
  ]
  action_row = manage_components.create_actionrow(*buttons)
  embed=discord.Embed(title='Privacy Policy', description='Please click the button below.', color=discord.Color.green())
  await ctx.send(embed=embed, components=[action_row])  

@bot.command()
async def amipro(ctx):
   prolist = ['You are Very Pro!', 'You are Pro', 'You are a mega pro']
   embed = discord.Embed(title='Pro: Random', description=random.choice(prolist), color=discord.Color.green())
   await ctx.send(embed=embed)

@bot.command()
async def credits(ctx):
    embed = discord.Embed(title='Credits', description='Credits for bot development, etc', color=discord.Color.green())
    embed.add_field(name='<@436312795076886528>', value='Bot Idea got by him')
    embed.add_field(name='discord.py', value='Bot Language')
    embed.add_field(name='<https://www.youtube.com/watch?v=gamozdALD9I>', value='uptimerobot.com tutorial')

    embed.add_field(name='repl.it', value='Hosting & Bot Development Help with definitions of some code')
    embed.add_field(name='Status', value='Credit to https://discord.com/channels/81384788765712384/381889733053251584/914196594440667166, credit: <@656919778572632094>')
    embed.add_field(name='https://www.youtube.com/watch?v=yeuuB7qiTbQ', value='Embed help')
    embed.add_field(name='https://discordpy.readthedocs.io/en/stable/whats_new.html?highlight=timeout', value='Basic Bot Development')
    embed.add_field(name='https://stackoverflow.com/questions/54418496/discord-py-how-do-i-send-private-message-to-someone-using-the-persons-id', value='Headstart of direct messages when added, basic base of it')
    embed.add_field(name='https://stackoverflow.com/questions/62834161/send-message-to-dms-discord-py', value='Direct Messages Help')
    embed.add_field(name='https://www.youtube.com/watch?v=CLQ8gfb2jh4', value='discord.py slash commands tutorial')
    embed.add_field(name='<@747386386490851349>', value='rm!randomfact idea')
    embed.add_field(name='google', value='rm!prealphanote command for the time in seconds')
    embed.add_field(name='https://www.advancedconverter.com/unit-conversions/time-conversion/years-to-seconds', value='Helping convert the year to seconds but seconds to seconds')
    embed.add_field(name='https://discord.com/channels/336642139381301249/381965515721146390/932085492953014302 and https://discord.com/channels/336642139381301249/381965515721146390/932085626814222376', value='Helping make hackbot command in premium of RandomMessages - asyncio.sleep()')
    embed.add_field(name='https://discord.com/channels/336642139381301249/381965515721146390/932086125273702490', value='Helping make hackbot command in premium of RandomMessages - editing')
    embed.add_field(name='https://discord.com/channels/336642139381301249/381965515721146390/932086337044111402', value='Helping make hackbot command in premium of RandomMessages - editing')
    embed.add_field(name='https://stackoverflow.com/questions/66510970/add-role-by-id-discord-py', value='Helping with bot event for when users use command, give role if in guild kinda like')
    embed.add_field(name='https://stackoverflow.com/questions/49352368/discord-py-delete-author-message-after-executing-command#:~:text=2%20Answers&text=You%20can%20obtain%20the%20message,delete_message%20coroutine%20to%20delete%20messages.', value='Helped with message deletion for the rm!say command')
     
     
@bot.command()
async def procommands(ctx):
     embed = discord.Embed(title='Pro Commands', description='Random Pro Commands', color = discord.Color.green())
     embed.add_field(name='rm!prorandom', value='Sends a random pro message')
     embed.add_field(name='rm!amipro', value='Sends a  random pro message, all messages sent are basically saying yes')
     embed.add_field(name='rm!aminoob', value='All answers say no')
     await ctx.send(embed=embed)

@bot.command()
async def prochecker(ctx):
   procheckerl = ['You are pro', 'Yes', 'You are']
   embed = discord.Embed(title='Pro Checker', description=random.choice(procheckerl), color=discord.Color.green())
   await ctx.send(embed=embed)

@bot.command()
async def randomuscoin(ctx):
      randomuscoinl = ['Nickel', 'Dime', 'Penny', 'Quarter', 'Half-Dollar Coin']
      embed = discord.Embed(title='Random US Coin', description=random.choice(randomuscoinl), color=discord.Color.green())
      embed.set_footer(text='The thing you get in the embed does not have any real value of money, this is just a fun command interactive.')
      await ctx.send(embed=embed)

@bot.command()
async def moneycommands(ctx):
      embed = discord.Embed(title='Money Commands', description='The thing you get in the embed of any of these commands does not have any real value of money, this is just a fun command interactive.', color=discord.Color.green())
      embed.add_field(name='rm!randomuscoin', value='Random US coin')
      embed.add_field(name='rm!norrandom', value='Nickel or dime command.')
      await ctx.send(embed=embed)

@bot.command()
async def moderationcommands(ctx):
      await ctx.send('Work in progress')

@bot.command()
async def botdevelopers(ctx):
     embed = discord.Embed(title='Bot Developers: RandomMessages', description='Bot Developers of RandomMessages Officially', color=discord.Color.green())
     embed.add_field(name='Chai_rbf#9987', value='Bot Development using sources. (see rm!credits for some)')
     embed.set_footer(text='Official Bot Developers', icon_url='https://media.discordapp.net/attachments/905518753033371738/921210998411644958/botimg.png?width=422&height=422')    
     await ctx.send(embed=embed)

@bot.command()
async def botfounder(ctx):
      embed = discord.Embed(title='Bot Founder', description='Founder of RandomMessages!', color=discord.Color.green())
      embed.add_field(name='Chai_rbf', value='Chai_rbf is the founder of RandomMessages.')
      embed.set_footer(text='Official Founder of RandomMessages', icon_url='https://media.discordapp.net/attachments/920449546339893282/931650326405189682/rm_nimg.png?width=422&height=422')   
      await ctx.send(embed=embed)


@bot.command()
@commands.has_role(920449565633687612)
async def statuschange(ctx):
       await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='random commands'))
       await ctx.send('Status Change accepted, I assume.')

           
@bot.command()
async def aminoob(ctx):
      aminoobrandom = ['No', 'You are not']
      embed = discord.Embed(title='rm!aminoob', description=random.choice(aminoobrandom), color=discord.Color.green()) 
      await ctx.send(embed=embed)

@bot.command()
async def trueorfalse(ctx):
      trueorfalse = ['True', 'False']
      embed = discord.Embed(title='True Or False', description=random.choice(trueorfalse), color=discord.Color.green())
      embed.set_footer(text='NOTICE: This does not represent any real value and this embed entirely is considered a joke for fun purposes. This does not represent anything real and has no value.')
      await ctx.send(embed=embed)

@bot.command()
async def timeout(ctx):
      timeoutr = ['Nah', 'Sure!', 'No']
      embed = discord.Embed(title='Timeout: New Discord Feature, Credit: Discord', description=random.choice(timeoutr), color=discord.Color.red())
      embed.set_footer(text='This does not represent a discord action and will not be given. This is for entertainment purposes.')
      await ctx.send(embed=embed)

            
@bot.command()
async def rate5stars(ctx):
       r5sl = [':star:', ':star: :star:', ':star: :star: :star:', ':star: :star: :star: :star:', ':star: :star: :star: :star: :star:']
       embed = discord.Embed(title='5 Stars: Rated', description=random.choice(r5sl), color=discord.Color.gold())
       embed.set_footer(text='This is meant for laughter and entertainment, not cyberbullying or bullying in ANY way. RandomMessages is not responsible for anything illegal happening over the "rm!rate5stars" command.')
       await ctx.send(embed=embed)

@bot.command()
async def bugreport(ctx):
     embed = discord.Embed(title='Bug Reporting', description='Hey! Bug reporting should be reported in the official support server (https://discord.gg/qgZpzUdGgg). Thank you!', color=discord.Color.green())
     await ctx.send(embed=embed)

@bot.command()
async def userreport(ctx):
      embed = discord.Embed(title='User Reporting', description='Hey! Reporting users should be reported in the official support server (https://discord.gg/qgZpzUdGgg). RandomMessages currently and may only support right now partnership user reporting. Thank you!', color=discord.Color.green())
      await ctx.send(embed=embed)
     
@bot.command()
async def support(ctx):     
     embed = discord.Embed(title='Support: RandomMessages', description='Please go to the help discord, the official one, of RandomMessages and ask members first. If the issue is unsolvable by members, please ask developers or staff. Help discord: https://discord.gg/qgZpzUdGgg', color=discord.Color.green())
     await ctx.send(embed=embed)

@bot.command()
async def supportcommands(ctx):
     embed = discord.Embed(title='Support Category: RandomMessages', description='Support commands for RandomMessages!', color=discord.Color.green())
     embed.add_field(name='rm!reportbug', value='Report bugs for RandomMessages!')
     embed.add_field(name='rm!reportuser', value='Report users for RandomMessages!')
     embed.add_field(name='rm!support', value='N/A')
     await ctx.send(embed=embed)


@bot.command()
async def developeronly(ctx):
       embed = discord.Embed(title='Developer-Only Commands', description='RandomMessages developer-only!', color=discord.Color.green())
       embed.add_field(name='rmdev!status.change',value='Adds bot status')
       await ctx.send(embed=embed)

@bot.command()
async def randomfact(ctx):
      rfrm = ['A developer of RandomMessages has wrote this message!', 'You are alive.', 'A pro is you.', '{} rocks!'.format(ctx.author.mention)]
      embed = discord.Embed(title='Random Fact', description='Random fact: {}'.format(random.choice(rfrm)), color=discord.Color.green())
      embed.set_footer(text='Random Fact')
      await ctx.send(embed=embed)

@bot.command()
async def moderation(ctx):
      embed = discord.Embed(title='Moderation: RandomMessages', description='Moderation commands!', color=discord.Color.red())
      embed.add_field(name='rm!timeout', value='The new discord timeout feature - this does not perform a real discord action')
      await ctx.send(embed=embed)

@bot.command()
async def funcommands(ctx):
      embed = discord.Embed(title='Fun Commands', description='Fun commands, in general!', color=discord.Color.green())
      embed.add_field(name='rm!rate5stars', value='Rates out of 5 stars! Command has a notice, please read.')
      embed.add_field(name='rm!trueorfalse', value='Says if something is true or false! Command has a notice, please read.')
      await ctx.send(embed=embed)
# pip install discord-py-slash-command
@bot.command()      
async def supportserver(ctx):
  buttons= [
    manage_components.create_button(
      style=ButtonStyle.URL,
      label="Support Server", url="https://discord.gg/qgZpzUdGgg"
    )
  ]
  action_row = manage_components.create_actionrow(*buttons)
  await ctx.send("Hey! Please click the button below for the link to the support server for now.", components=[action_row])

@bot.command()
@commands.has_any_role(927294248208990219, 927294287488639036)
async def staffpro(ctx):
  staffprolist = [f'you are very pro, {ctx.author.mention}!', f'{ctx.author.mention}, you are pro..', f'N/A, {ctx.author.mention} !', f'somewhat pro, {ctx.author.mention}']
  embed = discord.Embed(title=f'Are you pro: Staff version?', description=f'seems like {random.choice(staffprolist)}', color=discord.Color.green())
  await ctx.send(embed=embed)

@bot.command()
@commands.has_role(923224503843180604)
@commands.cooldown(1,31556926.000001, commands.BucketType.user)
async def prealphanote(ctx):
  embed = discord.Embed(title='To YOU,', description='Thank you for being a person who supported RandomMessages through the early times of the bot and times wherein the bot was not verified and was not in a lot of servers. You trusted RandomMessages and used it although it could have been a scam. Thank you.', color=discord.Color.green())
  embed.set_footer(text='Mostly by, - Chai_rbf')
  await ctx.author.send(embed=embed)

@bot.command()
@commands.has_role(920449615118090270)
async def say(ctx, *, arg):
  await ctx.message.delete()
  await ctx.send(arg)

@bot.command()
@commands.has_role(920449615118090270)
async def dm(ctx, user : discord.User, *, arg):
  await user.send(f"A message has been sent to you by {ctx.author.mention} saying: {arg}")

bot.run('TOKEN_HERE')
