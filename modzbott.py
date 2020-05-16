import discord
import asyncio
import json
import os
from discord.ext import commands


client = commands.Bot(command_prefix= '/')
token = 'NzA5MDMwMjYxNjA1NzkzODAz.XrqXIg.c-vwUsX-wQc7pTRO11qBOeDN45E'

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="/support"))
    print('Bot is ready.')

@client.event
async def on_member_join(member):
    with open('users.json', 'r') as f:
        users = json.load(f)

    await update_data(users, member)

    with open('users.json', 'w') as f:
        json.dump(users, f)


@client.event
async def on_message(message):
    if message.author.bot == False:
        with open('users.json', 'r') as f:
            users = json.load(f)

        await update_data(users, message.author)
        await add_experience(users, message.author, 5)
        await level_up(users, message.author, message)

        with open('users.json', 'w') as f:
            json.dump(users, f)


async def update_data(users, user):
    if not f'{user.id}' in users:
        users[f'{user.id}'] = {}
        users[f'{user.id}']['experience'] = 0
        users[f'{user.id}']['level'] = 1


async def add_experience(users, user, exp):
    users[f'{user.id}']['experience'] += exp


async def level_up(users, user, message):
    experience = users[f'{user.id}']['experience']
    lvl_start = users[f'{user.id}']['level']
    lvl_end = int(experience ** (1 / 4))
    if lvl_start < lvl_end:
        await message.channel.send(f'{user.mention} has leveled up to level {lvl_end}')
        users[f'{user.id}']['level'] = lvl_end

@client.command()
async def rename(ctx, channel: discord.VoiceChannel, *, new_name):
    await channel.edit(name=new_name)

@client.command()
async def support(ctx):
    embed = discord.Embed(title='/Support', description='**Join the ModzBott support server using this link:** https://discord.gg/nzEnYtZ\n\nA list of links has also been sent to your DMs', colour=discord.Colour.green())
    msg = await ctx.send(embed=embed)

    await ctx.message.delete()
    await ctx.author.send('**ModzBott Support Links:**\n\nhttps://github.com/Modzzzzz/ModzBott - github/\nhttps://top.gg/bot/709030261605793803 - Discord Bot Page\nhttps://discord.gg/nzEnYtZ - Support server')
    await asyncio.sleep(15)

    await msg.delete()

@client.command()
async def commands(ctx):
    embed=discord.Embed(title="/Commands", description="A list of commands has been sent to your DM's.", colour=discord.Color.blue())
    msg = await ctx.send(embed=embed)

    await ctx.message.delete()
    await ctx.author.send('**List of all available ModzBott commands:**')
    await asyncio.sleep(2)
    await ctx.author.send('/commands /support /rename')

    await asyncio.sleep(10)
    await msg.delete()

    await ctx.message.delete()
    await asyncio.sleep(15)
    await msg.delete()



client.run(token)