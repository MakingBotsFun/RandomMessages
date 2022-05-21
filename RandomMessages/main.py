import nextcord
import random
import os
import keep_alive
from nextcord.ext import commands
keep_alive.keep_alive()
from nextcord.ext import application_checks
client = nextcord.Client()
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

@bot.event
async def on_ready():
  await bot.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.watching, name="command execution"))



@bot.slash_command()
async def norrandom(interaction : nextcord.Interaction):
  class Norrandombuttons(nextcord.ui.View):
    def __init__(self):
      super().__init__()

    @nextcord.ui.button(label="Randomize", style=nextcord.ButtonStyle.green)
    async def send(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
      norlist = ['Nickel', 'Dime']
      embed = nextcord.Embed(title='Nickel Or Dime', description=random.choice(norlist),color=nextcord.Color.green())
      embed.set_footer(text='The thing you get in the embed does not have any real value of money, this is just a fun command interactive.')
      await interaction.send(embed=embed, ephemeral=True)
      self.stop()

    @nextcord.ui.button(label="Cancel", style=nextcord.ButtonStyle.red)
    async def cancel(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
      await interaction.send("Cancelled this action.", ephemeral=True)
      self.stop()

  View = Norrandombuttons()
  await interaction.send("Check nickel or dime?", view=View, ephemeral=True)

class SuggestionsModal(nextcord.ui.Modal):
  def __init__(self):
    super().__init__("Submit suggestion")
    self.ST = nextcord.ui.TextInput(label="Title", min_length=5, max_length=150, placeholder="Add suggestion title", required=True)
    self.add_item(self.ST)

    self.SD = nextcord.ui.TextInput(label="Suggestion Description", min_length=50, max_length=2500, placeholder="Describe your suggestion", required=True, style=nextcord.TextInputStyle.paragraph)
    self.add_item(self.SD)
  async def callback(self, interaction : nextcord.Interaction) -> None:
    title = self.ST.value
    desc = self.SD.value
    channel = await bot.fetch_channel(976546284850782238)
    embed = nextcord.Embed(title=f"{title} : RandomMessages", description=f"{desc}", color=nextcord.Color.green())
    embed.set_footer(text=f"Submitted by {interaction.user}, ID: {interaction.user.id}")
    return await channel.send(embed=embed)
   
@bot.slash_command(description="Suggest something to Making Bots Fun for RandomMessages!")
@commands.cooldown(1,500,commands.BucketType.user)
async def suggestions(interaction : nextcord.Interaction):
   await interaction.response.send_modal(SuggestionsModal()) 

@bot.slash_command(description="Are you pro?")
async def amipro(interaction : nextcord.Interaction):
  class ProButtons(nextcord.ui.View):
    def __init__(self):
      super().__init__()

    @nextcord.ui.button(label="Randomize", style=nextcord.ButtonStyle.green)
    async def send(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
      prolist = ['You are Very Pro!', 'You are Pro', 'You are a mega pro']
      embed = nextcord.Embed(title='Pro: Random', description=random.choice(prolist), color=nextcord.Color.green())
      await interaction.send(embed=embed, ephemeral=True)
      self.stop()

    @nextcord.ui.button(label="Cancel", style=nextcord.ButtonStyle.red)
    async def cancel(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
      await interaction.send("Cancelled this action.", ephemeral=True)
      self.stop()
  View = ProButtons()
  await interaction.send("Check if you are pro?", view=View, ephemeral=True)
     

@bot.slash_command(description="Checker for if you are pro")
async def prochecker(interaction : nextcord.Interaction):
  class Procheckerbuttons(nextcord.ui.View):
    def __init__(self):
      super().__init__()

    @nextcord.ui.button(label="Randomize", style=nextcord.ButtonStyle.green)
    async def send(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
       procheckerl = ['You are pro', 'Yes', 'You are']
       await interaction.send(random.choice(procheckerl), ephemeral=True)
       self.stop()

    @nextcord.ui.button(label="Cancel", style=nextcord.ButtonStyle.red)
    async def cancel(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
      await interaction.send("Cancelled this action.", ephemeral=True)
      self.stop()
  View = Procheckerbuttons()
  await interaction.send("Check if you are pro?", view=View, ephemeral=True)

@bot.slash_command(description="Random US coin!")
async def randomuscoin(interaction : nextcord.Interaction):
  class USCoinButtons(nextcord.ui.View):
    def __init__(self):
      super().__init__()

    @nextcord.ui.button(label="Randomize", style=nextcord.ButtonStyle.green)
    async def send(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
      randomuscoinl = ['Nickel', 'Dime', 'Penny', 'Quarter', 'Half-Dollar Coin']
      embed = nextcord.Embed(title='Random US Coin', description=random.choice(randomuscoinl), color=nextcord.Color.green())
      embed.set_footer(text='The thing you get in the embed does not have any real value of money, this is just a fun command interactive.')
      await interaction.send(embed=embed, ephemeral=True)
      self.stop()

    @nextcord.ui.button(label="Cancel", style=nextcord.ButtonStyle.red)
    async def cancel(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
      await interaction.send("Cancelled this action.", ephemeral=True)
      self.stop()
  View = USCoinButtons()
  await interaction.send("Check for a random coin", view=View, ephemeral=True)


@bot.slash_command("Check the bot developers!")
async def botdevelopers(interaction : nextcord.Interaction):
     embed = nextcord.Embed(title='Bot Developers: RandomMessages', description='Bot Developers of RandomMessages Officially', color=nextcord.Color.green())
     embed.add_field(name='Chai_rbf#9987', value='Bot Development using sources. (see rm!credits for some)')
     embed.set_footer(text='Official Bot Developers', icon_url='https://media.nextcordapp.net/attachments/905518753033371738/921210998411644958/botimg.png?width=422&height=422')    
     await interaction.send(embed=embed, ephemeral=True)

           
@bot.slash_command(description="Check if you are a noob!")
async def aminoob(interaction : nextcord.Interaction):
  class aminoobbuttons(nextcord.ui.View):
    def __init__(self):
      super().__init__()

    @nextcord.ui.button(label="Randomize", style=nextcord.ButtonStyle.green)
    async def send(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
      aminoobrandom = ['No', 'You are not']
      embed = nextcord.Embed(title='rm!aminoob', description=random.choice(aminoobrandom), color=nextcord.Color.green()) 
      await interaction.send(embed=embed)
      self.stop()

    @nextcord.ui.button(label="Cancel", style=nextcord.ButtonStyle.red)
    async def cancel(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
      await interaction.send("Cancelled this action.", ephemeral=True)
      self.stop()
  View = aminoobbuttons()
  await interaction.send("Check if you are a noob?", view=View, ephemeral=True)

@bot.slash_command(description="True or false?")
async def trueorfalse(interaction : nextcord.Interaction):
    class trueorfalsebuttons(nextcord.ui.View):
      def __init__(self):
        super().__init__()

      @nextcord.ui.button(label="Randomize", style=nextcord.ButtonStyle.green)
      async def send(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        trueorfalse = ['True', 'False']
        embed = nextcord.Embed(title='True Or False', description=random.choice(trueorfalse), color=nextcord.Color.green())
        embed.set_footer(text='NOTICE: This does not represent any real value and this embed entirely is considered a joke for fun purposes. This does not represent anything real and has no value.')
        await interaction.send(embed=embed, ephemeral=True)
        self.stop()
        
      @nextcord.ui.button(label="Cancel", style=nextcord.ButtonStyle.red)
      async def cancel(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.send("Cancelled this action.", ephemeral=True)
        self.stop()
    View = trueorfalsebuttons()
    await interaction.send("Check if true or false?", view=View, ephemeral=True)

            
@bot.slash_command(description="Let the bot rate out of 5 stars something!")
async def rate5stars(interaction : nextcord.Interaction):
    class r5sbuttons(nextcord.ui.View):
      def __init__(self):
        super().__init__()

      @nextcord.ui.button(label="Randomize", style=nextcord.ButtonStyle.green)
      async def send(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        r5sl = [':star:', ':star: :star:', ':star: :star: :star:', ':star: :star: :star: :star:', ':star: :star: :star: :star: :star:']
        embed = nextcord.Embed(title='5 Stars: Rated', description=random.choice(r5sl), color=nextcord.Color.gold())
        embed.set_footer(text='This is meant for laughter and entertainment, not cyberbullying or bullying in ANY way. RandomMessages is not responsible for anything illegal happening over the "rm!rate5stars" command.')
        embed.set_footer(text='NOTICE: This does not represent any real value and this embed entirely is considered a joke for fun purposes. This does not represent anything real and has no value.')
        await interaction.send(embed=embed, ephemeral=True)
        self.stop()

      @nextcord.ui.button(label="Cancel", style=nextcord.ButtonStyle.red)
      async def cancel(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.send("Cancelled this action.", ephemeral=True)
        self.stop()
    View = r5sbuttons()
    await interaction.send("Let the bot rate out of 5 stars?", view=View, ephemeral=True)

@bot.slash_command(description="Get the link to the support server!")
async def support(interaction : nextcord.Interaction):     
     embed = nextcord.Embed(title='Support: RandomMessages', description='Please go to the help support server, the official one, of RandomMessages and ask members first. If the issue is unsolvable by members, please ask developers or staff. Help support server: https://nextcord.gg/qgZpzUdGgg', color=nextcord.Color.green())
     await interaction.send(embed=embed, ephemeral=True)

@bot.slash_command(description="Random fact!")
async def randomfact(interaction : nextcord.Interaction):
  randomfactlist = ["An developer of this bot wrote this message.", "You are alive.", f"You are {interaction.user.mention}"]
  embed = nextcord.Embed(title="Random Fact", description=f"{random.choice(randomfactlist)}", color=nextcord.Color.green())
  embed.set_footer(text='Random Fact')
  await interaction.send(embed=embed, ephemeral=True)

@bot.slash_command(description="(For staff) See if you are pro!")
@commands.has_any_role(927294248208990219, 927294287488639036)
async def staffpro(interaction : nextcord.Interaction):
  staffprolist = [f"you are very pro, {interaction.user.mention}!", f"{interaction.user.mention}, you are pro.", f"N/A, {interaction.user.mention} !", f"somewhat pro, {interaction.user.mention}"]
  embed = nextcord.Embed(title=f"Are you pro: Staff version?", description=f"seems like {random.choice(staffprolist)}", color=nextcord.Color.green())
  await interaction.send(embed=embed, ephemeral=True)

@bot.slash_command(description="For pre-alpha users")
@commands.has_role(923224503843180604)
@commands.cooldown(1,31556926.000001, commands.BucketType.user)
async def prealphanote(interaction : nextcord.Interaction):
  embed = nextcord.Embed(title='To YOU,', description='Thank you for being a person who supported RandomMessages through the early times of the bot and times wherein the bot was not verified and was not in a lot of servers. You trusted RandomMessages and used it although it could have been a scam. Thank you.', color=nextcord.Color.green())
  embed.set_footer(text='Mostly by, - Chai_rbf')
  await interaction.user.send(embed=embed)

@bot.command()
@commands.has_role(920449615118090270)
async def say(ctx, *, arg):
  await ctx.message.delete()
  await ctx.send(arg)


@bot.command()
@commands.has_role(920449615118090270)
async def dm(ctx, user : nextcord.User, *, arg):
  await user.send(f"A message has been sent to you by {ctx.author.mention} saying: {arg}")

bot.run('TOKEN_HERE')
