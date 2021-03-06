# Bot imports
import discord
import asyncio
from discord.ext import commands
from webserver import keep_alive
import sys

# Registering moderation commands
sys.path.append('./commands/moderation/')
import clear
import kick
import ban

# Registering default bot commands
sys.path.append('./commands/default/')
import invite
import help
import information

# registering bot cogs to be launched on bot start
cogs = [invite, clear, information, help, kick, ban]

# All bots 0auth2 variables
token = '' # Removed for security reasons.
client = commands.Bot(command_prefix='s!')
client.remove_command('help')

# Code to be ran when the bot starts up
@client.event
async def on_ready():
  pp = True
  print('Scorpic online! Server online!')
  print('|')
  print('|')
  while pp == True:
      guilds = str(len(client.guilds))
      await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=f's!help | {guilds} servers!'))
      await asyncio.sleep(10)
      await client.change_presence(activity=discord.Activity
      (type=discord.ActivityType.playing, name=f's!invite | {guilds} servers!'))
      await asyncio.sleep(10)

# For loop to setup all cogs
for i in range(len(cogs)):
    cogs[i].setup(client)

# Keeping the bot alive and run the 0auth2 token
keep_alive()
client.run(token)
