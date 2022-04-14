import nextcord
from nextcord.ext import commands
from nextcord import Interaction, SlashOption, ChannelType
import json
import json
from pathlib import Path
from typing import Optional
import platform
import logging
import datetime
from nextcord.abc import GuildChannel
import datetime
from nextcord.ext import application_checks
import keep_alive
import random
keep_alive.keep_alive()


intents = nextcord.Intents.default()
intents.members = True



bot_version = "1.6 Public Release Version"

cwd = Path(__file__).parents[0]
cwd = str(cwd)

client = commands.Bot(command_prefix="ge!", help_command=None, intents=intents)



@client.event
async def on_ready():
  await client.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.watching, name=f"greenville sessions"))

@client.event
async def on_guild_join(guild):
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            await channel.send(":wave: Hey! Thanks for choosing GreenvilleSessions as a discord bot for you to use in your server. \n \n \n This message will go over a few things you should do first. \n \n 1. Use the /botguide command for your server. This will be very useful to help you setup GreenvilleSessions in your server. \n \n 2. Look at the possible errors using /possibleerrors. \n \n 3. Understand that all startup commands or most will not respond to you unless you correctly do steps 1 and 2 of the bot guide. \n \n 4. Have any issues? Report it on the github general help's issues (<https://github.com/MakingBotsFun/General-Help/issues>) \n \n Thanks, \n Chai_rbf, \n Founder, \n Making Bots Fun ")
        break
      
mentions_true = allowed_mentions=nextcord.AllowedMentions(everyone=True)

client.blacklisted_users = []



def read_json(filename):
    with open(f"{cwd}/{filename}.json", "r") as file:
        data = json.load(file)
    return data

def write_json(data, filename):
    with open(f"{cwd}/{filename}.json", "w") as file:
        json.dump(data, file, indent=4)  

data = read_json("blacklist")
client.blacklisted_users = data["blacklistedUsers"]
  
# @client.application_command_check
# async def check_commands(interaction: nextcord.Interaction) -> bool:
 #  if interaction.user.id in client.blacklisted_users:
  #   await interaction.send("You are blacklisted from using the bot.", ephemeral=True)
 #   return False
 # else:
  #  return True

@application_checks.has_role("GreenvilleSessions Host")
@client.slash_command(description="Startup a session!")
async def startupsession(interaction : nextcord.Interaction, requiredreactions : int):
  embed = nextcord.Embed(title="Session Startup", description=f"Hey everyone! \n \n \n A session has started by {interaction.user.mention}. Please make sure to read the important channels that are in this server before joining the session. \n \n \n Make sure to respect server staff who host sessions, and follow any directions given by them. \n \n \n To join the session, make sure in your roblox settings in the privacy tab everyone can invite you. \n \n \n Make sure to react to this message after doing so with the checkmark. {requiredreactions} are required for the session to start.", color=nextcord.Color.green())
  await interaction.send("Sending! Expect the message to appear shortly.", ephemeral=True)
  msg = await interaction.channel.send("@here", embed=embed, allowed_mentions=mentions_true)
  await msg.add_reaction("✅")


@application_checks.has_role("GreenvilleSessions Host")
@client.slash_command(description="Make the bot send a message that you are setting up a server!")
async def settingup(interaction : Interaction):
  embed = nextcord.Embed(title="Setting Up", description=f"The session is being set up by {interaction.user.mention}. Please get ready to join the session soon.", color=nextcord.Color.green())
  await interaction.response.send_message(embed=embed)

@application_checks.has_role("GreenvilleSessions Host")
@client.slash_command(description="Make the bot send a message of who the co-hosts are!")
async def cohosts(interaction : Interaction, cohost : nextcord.Member, cohost2 : Optional[nextcord.Member]):
  if not cohost2:   
    embed = nextcord.Embed(title="Co-host decided", description=f"The co-host for this session has been decided! The co-host: {cohost.mention}", color=nextcord.Color.green())
    await interaction.response.send_message(embed=embed)
  else:
    embed = nextcord.Embed(title="Co-hosts decided", description=f"The co-hosts for this session have been decided! The co-hosts: {cohost.mention} and {cohost2.mention}.", color=nextcord.Color.green())
    await interaction.send(embed=embed)

@application_checks.has_role("GreenvilleSessions Host")
@client.slash_command(description="Tell people that you released a server!")
async def sessionrelease(interaction : nextcord.Interaction, link : str):
  embed = nextcord.Embed(title="Session Released", description=f"{interaction.user.mention}'s session has been released! \n \n The link: {link}", color=nextcord.Color.green())
  if link.startswith("https://www.roblox.com/games/"):
    await interaction.send("Success! Sending shortly.", ephemeral=True)
    await interaction.channel.send("@here", embed=embed, allowed_mentions=mentions_true)
  else:
    await interaction.send("GREENVILLESESSIONS_DETECTION: Not roblox vip server link", ephemeral=True)

@application_checks.has_role("GreenvilleSessions Host")
async def earlyaccess(interaction : nextcord.Interaction, link : str):
  embed = nextcord.Embed(title="Early Access", description=f"{interaction.user.mention}'s session has got released for early access members! The link: {link}", color=nextcord.Color.blue())
  if link.startswith("https://www.roblox.com/games/"):
    await interaction.send(embed=embed)
  else:
    await interaction.send("GREENVILLESESSIONS_DETECTION: Not roblox vip server link", ephemeral=True)
    
    
@client.slash_command(description="View the guide for GreenvilleSessions!")
async def botguide(interaction : nextcord.Interaction):
  embed = nextcord.Embed(title=":wave: Hey there!", description="Thank you for choosing GreenvilleSessions for your server. This guide will show you how to make GreenvilleSessions working, as most of the commands will not work without the setup of the bot. \n \n Instructions \n \n 1. Make a role in your discord server called GreenvilleSessions Host. \n \n 2. Give the role to the staff members who you allow to host sessions in your server. \n \n 3. Try the bot now. If the commands aren't working, maybe try looking at the possible errors of the bot using the /possibleerrors command. \n \n \n Extra: Tired of adding roles to your staff? Make a role called GreenvilleSessions Administrator, and use the /addroles command. It helps a ton! \n \n \nThat's all, thank you for using GreenvilleSessions! If you need any help, don't feel afraid to join the support server.", color=nextcord.Color.green())
  if interaction.guild.owner_id == interaction.user.id:
    await interaction.send(embed=embed, ephemeral=True)
  else:
    await interaction.send("You do not have permission to use this command. Only the server owner can.", ephemeral=True)

@client.slash_command(description="Look at the possible errors of the bot!")
async def possibleerrors(interaction : nextcord.Interaction):
  embed = nextcord.Embed(title="Possible Errors", description="1. The bot is not responding! \n **Solution: Try looking at /botguide. If you can't reach that and the slash commands do not work for a long time, go to the support server and talk with the staff.** \n \n 2. My staff can't host with the bot, even though I created the role GreenvilleSessions Host! \n **Solution: This would be because you didn't give your staff members who can host the role. If this is not the case, go to the support server and talk with the staff.**", color=nextcord.Color.green())
  await interaction.send(embed=embed, ephemeral=True)


@commands.has_role(930193112201064581)
@client.command()
async def contactdm(ctx, member : nextcord.Member, *, arg):
  await ctx.message.delete()
  await ctx.author.send(f":white_check_mark: It seems that your message has been sent to {member.mention}. Your message: {arg}")
  await member.send(f"A message was sent to you by the founder of Making Bots Fun officially, {ctx.author.mention}. Message:", arg)


@commands.has_role(930193112201064581)
@client.command()
async def saymessage(ctx, *, arg):
  await ctx.message.delete()
  await ctx.send(arg)

@client.slash_command(description="End a session!")
async def endsession(interaction : nextcord.Interaction):
  embed = nextcord.Embed(title="Session Ended", description=f"The session by {interaction.user.mention} has ended.", color=nextcord.Color.red())
  await interaction.send(embed=embed)

@client.slash_command(description="Cancel a session!")
async def cancelsession(interaction : nextcord.Interaction):
  embed = nextcord.Embed(title="Session Cancelled", description=f"{interaction.user.mention}'s session has ended.", color=nextcord.Color.red())
  await interaction.send(embed=embed)


@client.slash_command(description="View the credits of the bot!")
async def credits(interaction : nextcord.Interaction):
  embed = nextcord.Embed(title="Credits", description="Credits: \n \n 1. Nextcord for the library of the bot \n \n 2. https://gist.github.com/0xicl33n/e5008c5865347aafc644a67455507314 for the bot join message \n \n 3. <@744147607697489941> for the vehicle registration command idea \n \n That's all mostly!", color=nextcord.Color.green())
  await interaction.send(embed=embed, ephemeral=True)

@application_checks.has_role(920449615118090270)
@client.slash_command(description="Blacklist a user!")
async def blacklist(interaction : nextcord.Interaction, user : nextcord.User):
  
    client.blacklisted_users.append(user.id)
    data = read_json("blacklist")
    data["blacklistedUsers"].append(user.id)
    write_json(data, "blacklist")
    await interaction.send(f"Successfully blacklisted {user.mention}.", ephemeral=True)

@application_checks.has_role(920449615118090270)
@client.slash_command()
async def unblacklist(interaction : nextcord.Interaction, user : nextcord.User):
    client.blacklisted_users.remove(user.id)
    data = read_json("blacklist")
    data["blacklistedUsers"].remove(user.id)
    write_json(data, "blacklist")
    await interaction.send(f"Successfully unblacklisted {user.mention}.", ephemeral=True)


@client.slash_command(description="Get a link to the support server!")
async def supportserver(interaction : nextcord.Interaction):
  embed = nextcord.Embed(title="Support Server", description="A invite to the support server: https://discord.gg/qgZpzUdGgg", color=nextcord.Color.green())
  await interaction.send(embed=embed, ephemeral=True)

@client.slash_command(description="Look at the version of GreenvilleSessions at the moment!")
async def version(interaction : nextcord.Interaction):
  embed = nextcord.Embed(title="GreenvilleSessions Version", description=f"Current version: {bot_version} \n \n \n RELEASE NOTES FOR 1.6: \n - Added vehicle registration command thanks to <@744147607697489941>", color=nextcord.Color.green())
  await interaction.send(embed=embed, ephemeral=True)

@client.slash_command(description="Invite the bot!")
async def invite(interaction : nextcord.Interaction):
  embed = nextcord.Embed(title="Inviting the bot!", description="You can invite the bot with the link: https://discord.com/api/oauth2/authorize?client_id=961699072140521553&permissions=412317183040&scope=bot%20applications.commands", color=nextcord.Color.green())
  await interaction.send(embed=embed)


@application_checks.has_role("GreenvilleSessions Administrator")
@client.slash_command(description="Add a role to a user!")
async def addrole(interaction, needed_role: nextcord.Role, give: nextcord.Role): 
  for member in needed_role.members:
    await member.add_roles
   
  await interaction.send("Success!", ephemeral=True)
                           
  

@client.slash_command(description="Register a car!")
async def registervehicle(interaction : nextcord.Interaction, type : str, brand : str,  plate : str):
  embed = nextcord.Embed(title="Vehicle Registration", description=f"A vehicle has been registered by {interaction.user.mention}! Information: \n \n Type: {type} \n \n Brand: {brand} \n \n License Plate: {plate}", color=nextcord.Color.green())
  await interaction.send(embed=embed)
    
client.run("TOKEN_HERE")
