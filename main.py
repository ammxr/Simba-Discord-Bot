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
WEBHOOK_URL = "<redacted>"

from aiohttp import ClientSession
bot = commands.Bot(command_prefix='s-', intents=intents)

bot.remove_command('help')
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="Simmy Pics all day", url=""))
    print('Bot Ready')
@bot.command(pass_context = True)
async def meme(ctx):
    embed = discord.Embed(title="Simmy Bot | Meme Source.", description=None, color=0x709198)
    async with aiohttp.ClientSession() as cs:
      async with cs.get('https://www.reddit.com/r/memes/new.json?sort=hot') as r:
        res = await r.json()
        embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
        await ctx.send(embed=embed, content=None)
@bot.command(pass_context = True)
async def dp(ctx):
    embed = discord.Embed(title="Simmy Bot | Dog Source.", description=None, color=0x709198)
    async with aiohttp.ClientSession() as cs:
      async with cs.get('https://www.reddit.com/r/dogpictures/new.json?sort=hot') as r:
        res = await r.json()
        embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
        await ctx.send(embed=embed, content=None)

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

@bot.command()
async def ping(ctx):
    await ctx.send('Pong! {0}'.format(round(bot.latency, 1)))
@bot.command()
async def whatisreannesfavlabelslashsinger(ctx):
    await ctx.send('404collective and 404 4L')
@bot.command()
async def whoisthelegendarycreatorofthisloduinsanebot(ctx):
    await ctx.send('obv Spxdezzz#0024')
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

ifDog= ['dog', 'simmy', 'Simmy', 'SIMMY', 'DOG', 'Dog']
@bot.listen('on_message')
async def simmypics(message):
    if message.content.startswith( tuple(ifDog) ):
        embedVar = discord.Embed(title="Here's your Daily dose of Simmy...",color=0x709198)
        embedVar.set_image(url=random.choice(pics)) 
        await message.channel.send(embed=embedVar)
        await bot.process_commands(message)

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


@bot.command(description="Mutes the specified user.")
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, *, reason=None):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")

    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)
    f = discord.File("jamalsimmy1.png")
    embed = discord.Embed(title=":octagonal_sign:-----| Muted User | -----:octagonal_sign: ", description=f"{member.mention} was muted ", color= 0x709198)
    embed.add_field(name="Reason:", value=reason, inline=False)
    embed.set_image(url="attachment://jamalsimmy1.png")
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
    embed = discord.Embed(title=f"**Welcome to {guild} !!!**", description=f" <a:bluearrowright:823653950501683250>  {mention} Welcome to {guild}  <a:bluearrowleft:823654338844033045>\n We hope you enjoy your stay! Be sure to check out our... \n <:whitebullet:823656573032726531> - <#800451759839510548> \n <:whitebullet:823656573032726531> - <#800457142351298611> \n <:whitebullet:823656573032726531> - <#803911543346823168>", color = 0x709198)
    embed.set_footer(text=f"Current Member Count {guild.member_count}")
    f = discord.File("profile.png")
    embed.set_image(url="attachment://profile.png")
    #channel = discord.utils.get(member.guild.channels, id=800452330582704158)
    channel = bot.get_channel(int(819014660253679617))
    await channel.send(file=f, embed=embed)

#oo u makin simmy pissed rn say sike rn in the next 2 seconds or else... be ready for consequences...

@bot.event
async def on_member_remove(member: discord.Member = None):
    mention = member.mention
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
    f = discord.File("leave.png")
    embed.set_image(url="attachment://leave.png")
    channel = bot.get_channel(int(819014660253679617))
    await channel.send(file=f, embed=embed)

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


@bot.command()
async def rps(ctx, member: discord.Member):
  await ctx.author.send("Please enter your choice RPS")
  def check(m):
    return not m.guild and m.author == ctx.author
  resp1 = await bot.wait_for('message', check=check)
  await member.send("Please enter your choice RPS")
  def check2(m1):
    return not m1.guild and m1.author.id == member.id
  resp2 = await bot.wait_for('message', check=check2)
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




""""
@bot.command()
async def vc(ctx,member: discord.Member=None):
  guild = bot.get_guild(800451154286477342)
  channel = bot.get_channel(819014660253679617)
  if member is not None:
    voice_state = ctx.author.voice
  if voice_state is None:
      # Exiting if the user is not in a voice channel
      return await channel.message.send('godezzz isa capper')
  else: 
    return await channel.message.send('godezzz isa napper')
@bot.command()
async def foo(ctx,member: discord.Member=None):
    channel = 763588828615147526
    voice_state = ctx.channel.voice
    if voice_state is None:
        # Exiting if the user is not in a voice channel
        return await ctx.send('Member NOT in vc')
    if voice_state is not None:
        return await ctx.send('Member IS in vc')
@bot.command()
async def tst(ctx):
  voice_state = ctx.author.voice
  if voice_state is None:
    return await ctx.send('IVC*')
  if voice_state is not None:
    return await ctx.send('NIVC*') 
"""
bot.run("ODExMjk1NjAxOTAzMTQwOTg1.YCwH6A.FHg_psLmYpEhP00qw8AGgZAUSaE")
