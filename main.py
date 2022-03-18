#Client work: Simba Dog Bot
import discord
from discord.ext import commands
import datetime
from urllib import parse, request
import re
import random
import asyncio
import aiohttp
from PIL import Image
from io import BytesIO
intents = discord.Intents.default()
intents.members = True
from PIL import ImageFont
from PIL import ImageDraw 
import json
from aiohttp import ClientSession
WEBHOOK_URL = "<redacted>"
from discord import File

#JSON DUMPS | Prefixes + Welcome/Leave Channels --------------------------------
def get_prefix(client, message):
  with open ("prefixes.json", "r") as f:
    prefixes=json.load(f)
    return prefixes[str(message.guild.id)]
def get_welcome_channel(client, message):
  with open ("welcomechannel.json", "r") as f:
    welcome=json.load(f)
    return welcome[str(message.guild.id)]
def get_goodbye_channel(client, message):
  with open ("goodbyeChannel.json", "r") as f:
    goodbye=json.load(f)
    return goodbye[str(message.guild.id)]
bot = commands.Bot(command_prefix=get_prefix, intents=intents)

#Default Settings for Member Join message
@bot.event
async def on_guild_join(guild):
  #Prefixes Defaults
  with open ("prefixes.json", "r") as f:
    prefixes=json.load(f)
  prefixes[str(guild.id)] = "s-"
  with open ("prefixes.json", "w") as f:
    json.dump (prefixes, f, indent=4)
  #Welcome Defaults
  with open ("welcomechannel.json", "r") as f:
    welcome=json.load(f)
  welcome[str(guild.id)] = "n/a"
  with open ("welcomechannel.json", "w") as f:
    json.dump (welcome, f, indent=4)
  #Goodbye Defaults
  with open ("goodbyeChannel.json", "r") as f:
    goodbye=json.load(f)
  goodbye[str(guild.id)] = "n/a"
  with open ("goodbyeChannel.json", "w") as f:
    json.dump (goodbye, f, indent=4)

#Default Settings for Member Leave message
@bot.event
async def on_guild_remove(guild):
  with open ("prefixes.json", "r") as f:
    prefixes=json.load(f)
    prefixes.pop[str(guild.id)]
  with open ("prefixes.json", "w") as f:
    json.dump (prefixes, f, indent=4)
  with open ("welcomechannel.json", "r") as f:
    welcome=json.load(f)
    welcome.pop[str(guild.id)]
  with open ("welcomechannel.json", "w") as f:
    json.dump (welcome, f, indent=4)
  with open ("goodbyeChannel.json", "r") as f:
    goodbye=json.load(f)
    goodbye.pop[str(guild.id)]
  with open ("goodbyeChannel.json", "w") as f:
    json.dump (goodbye, f, indent=4)

#Custom prefix / Change prefix command
@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def prefix(ctx, prefix):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
    prefixes[str(ctx.guild.id)] = prefix
    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)
    await ctx.send(f'Prefix changed to: {prefix}')
@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def welcome(ctx):
    with open('welcomechannel.json', 'r') as f:
        welcome = json.load(f)
    welcome[str(ctx.guild.id)] = ctx.channel.id
    with open('welcomechannel.json', 'w') as f:
        json.dump(welcome, f, indent=4)
    await ctx.send(f'Welcome Channel Set!')
@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def goodbye(ctx):
    with open('goodbyeChannel.json', 'r') as f:
        goodbye = json.load(f)
    goodbye[str(ctx.guild.id)] = ctx.channel.id
    with open('goodbyeChannel.json', 'w') as f:
        json.dump(goodbye, f, indent=4)
        await ctx.send(f'Goodbye Channel Set!')

#BOT READY---------------------------------------------
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="Simmy Pics all day", url=""))
    print('Bot Ready')
@bot.command()
async def ping(ctx):
    await ctx.send('Pong! {0}'.format(round(bot.latency, 1)))
bot.remove_command('help')
@bot.group(invoke_without_command=True)
async def help(ctx):
  em = discord.Embed(title ="Command List", color= 0x709198)
  em.add_field(name ="Dog Pics          ", value = "s-dp               ", inline=False)
  em.add_field(name ="Memes             ", value = "s-meme             ", inline=False)
  em.add_field(name ="Rock Paper Scissors             ", value = "s-rps             ", inline=False)
  em.add_field(name ="Cap r8            ", value = "s-cap (@)             ", inline=False)
  em.add_field(name ="Mute/Unmute       ", value = "s-(un)mute (reason)", inline=False)
  em.add_field(name ="Fake Msgs         ", value = "s-msg (@)          ", inline=False)
  em.add_field(name ="Server Info       ", value = "s-info             ", inline= False)
  em.add_field(name ="Member Info       ", value = "s-whois            ", inline=False)
  em.set_thumbnail(url="https://i.ibb.co/zSJ78vW/Untitled.png")
  await ctx.send(embed= em)
pics = ["https://i.ibb.co/hWmz2q9/dog1.jpg",
          "https://i.ibb.co/f2c9pnV/dog2.jpg",
          "https://i.ibb.co/Y22qt1p/dog3.jpg",
          "https://i.ibb.co/0DcxGJp/dog4.jpg",
          "https://i.ibb.co/bLSLv8y/dog5.jpg",
          "https://i.ibb.co/5Gq4wKD/dog6.jpg",
          "https://i.ibb.co/rksn8cr/dog7.jpg",
          "https://i.ibb.co/YpsG9Dt/dog8.jpg",
          "https://i.ibb.co/zfZ0K8g/dog9.jpg",
          "https://i.ibb.co/bR0WnQ1/dog10.jpg",
          "https://i.ibb.co/2WrcdPX/dog11.jpg",
          "https://i.ibb.co/J3XkHWz/dog12.jpg",
          "https://i.ibb.co/279SqVM/dog13.jpg",
          "https://i.ibb.co/6WQ13mD/dog14.jpg",
          "https://i.ibb.co/zxKPQpD/dog15.jpg",
          "https://i.ibb.co/QDKgcwS/dog16.jpg",
          "https://i.ibb.co/pxD2c3k/dog17.jpg",
          "https://i.ibb.co/R2stKgB/dog18.jpg",
          "https://i.ibb.co/FXJyHRC/dog19.jpg",
          "https://i.ibb.co/0Y6WYZn/dog20.jpg",
          "https://i.ibb.co/LQGZ5LF/dog21.jpg",
          "https://i.ibb.co/G0VpXdL/dog22.jpg",
          "https://i.ibb.co/nfp0DYs/dog23.jpg",
          "https://i.ibb.co/TKSb5RN/dog24.jpg",
          "https://i.ibb.co/mB68NMd/dog25.jpg",
          "https://i.ibb.co/vjjv9K1/gdfgsfgs.jpg",
          "https://i.ibb.co/3yqX0Ky/imagezxzx0.jpg",
          "https://i.ibb.co/NTczghH/imagfdsgsdfge0.jpg",
          "https://i.ibb.co/FWPpNmD/xZ.jpg",]

#BOT COMMANDS ---------------------------------------------
@bot.command(pass_context = True)
async def meme(ctx):
    embed = discord.Embed(title="Simmy Bot | Meme Source.", description=None, color=0x709198)
    async with aiohttp.ClientSession() as cs:
      async with cs.get('https://www.reddit.com/r/memes/new.json?sort=hot') as r:
        res = await r.json()
        embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
        await ctx.send(embed=embed, content=None)

#Random Dog pics from Reddit
@bot.command(pass_context = True)
async def dp(ctx):
    embed = discord.Embed(title="Simmy Bot | Dog Source.", description=None, color=0x709198)
    async with aiohttp.ClientSession() as cs:
      async with cs.get('https://www.reddit.com/r/dogpictures/new.json?sort=hot') as r:
        res = await r.json()
        embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
        await ctx.send(embed=embed, content=None)

#Random Lie test (percentage) 
@bot.command()
async def cap(ctx,user:discord.User):
    num1 = 0
    num2 = 100
    try:
        numb = int(num1)
        numb = int(num2)
        value = random.randint(min(num1, num2), max(num1, num2))
        embedVar = discord.Embed(title= "Cap r8 machine",description = f"Hmm :thinking: {user.mention} dk bout that one, it lookin {value}% :billed_cap: to me ", color=0x709198)
        embedVar.set_thumbnail(url="https://i.ibb.co/8myYvKn/cap.png")
        await ctx.send(embed=embedVar)
    except:
        await ctx.send(embed=embedVar)

#Trigger response with random Simba dog pictures
ifDog= ['dog', 'simmy', 'Simmy', 'SIMMY', 'DOG', 'Dog']
@bot.listen('on_message')
async def simmypics(message):
    if message.content.startswith( tuple(ifDog) ):
        embedVar = discord.Embed(title="Here's your Daily dose of Simmy...",color=0x709198)
        embedVar.set_image(url=random.choice(pics)) 
        await message.channel.send(embed=embedVar)
        await bot.process_commands(message)

#Moderation | Server Info
@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="Server information brought to you by Simmy Bot", timestamp=datetime.datetime.utcnow(), color=0x709198)
    embed.add_field(name="Owner", value=f"{ctx.guild.owner}", inline=False)
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}", inline=False)
    embed.add_field(name="Member Count", value=f"{ctx.guild.member_count}", inline=False)
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}", inline=False)
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}", inline=False)
    embed.set_thumbnail(url=ctx.guild.icon_url)
    await ctx.send(embed=embed)

#Moderation | Mute/Unmute Member
@bot.command(description="Mutes the specified user.")
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, *, reason=None):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")

    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)
    f = discord.File("gangsterSimmy1.png")
    embed = discord.Embed(title=":octagonal_sign:-----| Muted User | -----:octagonal_sign: ", description=f"{member.mention} was muted ", color= 0x709198)
    embed.add_field(name="Reason:", value=reason, inline=False)
    embed.set_image(url="attachment://gangsterSimmy1.png")
    await ctx.send(file=f, embed=embed)
    await member.add_roles(mutedRole, reason=reason)
    if reason==None:
      await member.send(f" L imaging getting muted in {guild.name} ")
    else:
      await member.send(f" L imaging getting muted in {guild.name} , especially for this reason '{reason}'")

@bot.command(description="Unmutes a specified user.")
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
   mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")
   await member.remove_roles(mutedRole)
   await member.send(f" You have been unmuted from: - {ctx.guild.name}")
   f = discord.File("simmyfly.png")
   embed = discord.Embed(title=":white_check_mark:-----| Unmuted User | -----:white_check_mark: ", description=f" Unmuted-{member.mention} fly free young one :pensive:",color = 0x709198)
   embed.set_image(url="attachment://simmyfly.png")
   await ctx.send(file=f, embed=embed)

# Welcome Member + Compiled picture
@bot.event
async def on_member_join(member):
    mention = member.mention
    compiled = Image.open ("background.png")
    testoverlay = Image.open ("testoverlay.png")
    outline = Image.open ("outline.png")
    asset= member.avatar_url_as(size = 128)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)
    pfp = pfp.resize((349,349))
    compiled.paste(pfp, (75,122))
    compiled.paste(outline, mask=outline)
    compiled.paste(testoverlay, mask=testoverlay)
    compiled.save("profile.png")
    guild = member.guild
    embed = discord.Embed(title=f"**Welcome to {guild} !!!**", description=f" <a:bluearrowright:823653950501683250>  {mention} Welcome to {guild}  <a:bluearrowleft:823654338844033045>\n Enjoy your stay!!!", color = 0x709198)
    embed.set_footer(text=f"Current Member Count {guild.member_count}")
    PicFile = discord.File("profile.png")
    embed.set_image(url="attachment://profile.png")
    with open("welcomechannel.json", "r") as f:
      welcome = json.load(f)
      channelValue = welcome[str(member.guild.id)]
    channel = bot.get_channel(channelValue)
    await channel.send(file=PicFile, embed=embed)

# Goodbye Member + Compiled picture
@bot.event
async def on_member_remove(member: discord.Member = None):
    mention = member.mention
    guild = member.guild
    leaveBase = Image.open ("leaveBase.png")
    leaveOverlay = Image.open ("leaveOverlay.png")
    asset = member.avatar_url_as(size=128)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)
    pfp = pfp.resize((129,129))
    leaveBase.paste(pfp, (359,423))
    leaveBase.paste(leaveOverlay, mask=leaveOverlay)
    leaveBase.save("leave.png")
    embed = discord.Embed(title="**Member Byeked!**", description=f"Byek {mention}!!!", color = 0x709198)
    embed.set_footer(text=f"Current Member Count {guild.member_count}")
    PicFile = discord.File("leave.png")
    embed.set_image(url="attachment://leave.png")
    with open("goodbyeChannel.json", "r") as f:
      goodbye = json.load(f)
      channelValue = goodbye[str(member.guild.id)]
    channel = bot.get_channel(channelValue)
    await channel.send(file=PicFile, embed=embed)

# Disguised Message sent to appear as if from a chosen user (Using webhooks)
@bot.command()
async def msg(ctx, member: discord.Member, *, message=None):
        if message == None:
                await ctx.send(f'Must specify a message')
                return
        webhook = await ctx.channel.create_webhook(name=member.name)
        await webhook.send(
            str(message), username=member.name, avatar_url=member.avatar_url)
        webhooks = await ctx.channel.webhooks()
        for webhook in webhooks:
                await webhook.delete()
                
# Moderation | Member Info
@bot.command()
async def whois(ctx, member: discord.Member = None):
    if not member:  # if member is no mentioned
        member = ctx.message.author  # set member as the author
    roles = [role for role in member.roles]
    embed = discord.Embed(colour=0x709198, timestamp=ctx.message.created_at,
                          title=f"User Info - {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Requested by {ctx.author}")

    embed.add_field(name="ID:", value=member.id)
    embed.add_field(name="Display Name:", value=member.display_name)

    embed.add_field(name="Created Account On:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name="Joined Server On:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name="Roles:", value="".join([role.mention for role in roles]))
    embed.add_field(name="Highest Role:", value=member.top_role.mention)
    print(member.top_role.mention)
    await ctx.send(embed=embed)

#Custom Rock, Paper, Scissors command DMs for input sends results in Server (Cheat proof) 
@bot.command()
async def rps(ctx, member: discord.Member):
  await ctx.author.send("Please enter your choice RPS")
  def check(m):
    return not m.guild and m.author == ctx.author
  resp1 = await bot.wait_for('message', check=check)
  await ctx.author.send(resp1.content)
  await member.send("Please enter your choice RPS")
  def check2(m1):
    return not m1.guild and m1.author.id == member.id
  resp2 = await bot.wait_for('message', check=check2)
  await member.send(resp2.content)
  #Winning Scenarios for response1
  response1=resp1.content.lower()
  response2=resp2.content.lower()
  if response1=="r" and response2=="s":
    await ctx.send(f" {ctx.author.mention} Won!!!")
  if response1=="p" and response2=="r":
    await ctx.send(f" {ctx.author.mention} Won!!!")
  if response1=="s" and response2=="p":
    await ctx.send(f" {ctx.author.mention} Won!!!")
  #Losing Scenarios for response1
  if response1=="r" and response2=="p":
    await ctx.send(f" {member.mention} Won!!!")
  if response1=="p" and response2=="s":
    await ctx.send(f" {member.mention} Won!!!")
  if response1=="s" and response2=="r":
    await ctx.send(f" {member.mention} Won!!!")
  #Draw
  if response1=="r" and response2=="r":
    await ctx.send(f" {ctx.author.mention} and {member.mention} TIED!!!")
  if response1=="p" and response2=="p":
    await ctx.send(f" {ctx.author.mention} and {member.mention} TIED!!!")
  if response1=="s" and response2=="s":
    await ctx.send(f" {ctx.author.mention} and {member.mention} TIED!!!")



#TicTacToe
@bot.command()
async def ttt(ctx, p2: discord.Member):
  # Global variables
  global tileChosen
  global count
  global player1
  global player2
  global turn
  global gameOver

  # Coordinates for Tiles
  global tile1
  global tile2
  global tile3
  global tile4
  global tile5
  global tile6
  global tile7
  global tile8
  global tile9

  tile1=(4,4)
  tile2=(108,4)
  tile3=(215,4)
  tile4=(4,108)
  tile5=(108,108)
  tile6=(215,108)
  tile7=(4,215)
  tile8=(108,215)
  tile9=(215,215)
  tileChosen=None

  #  Defaults Init
  p1 = ctx.author
  player1 = p1
  player2 = p2
  squaresTaken=0
  squaresTakenList=[]
  winner=None

#ADDONS ---------------------------------------------
@bot.command()
async def whatisreannesfavlabelslashsinger(ctx):
    await ctx.send('404collective and 404 4L')
@bot.command()
async def whoisthelegendarycreatorofthisloduinsanebot(ctx):
    await ctx.send('obv Spxdezzz#0024')



#BOT RUN---------------------------------------------
bot.run("TOKEN")
