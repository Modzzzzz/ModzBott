import discord
import asyncio
import random
import sqlite3
from discord.ext import commands
from webserver import keep_alive

token = ''
client = commands.Bot(command_prefix='m/')
client.remove_command('help')

@client.event
async def check(message):
    return message.author not in message.guild.members

@client.event
async def on_ready():
    db = sqlite3.connect('main.sqlite')
    cursor = db.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS main(
        guild_id TEXT,
        msg TEXT,
        channel_id TEXT
        )
        ''')
    print('ModzBott online! Server online!')
    while True:
        servers = str(len(client.guilds))
        await client.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.listening, name=f'{servers} servers!'))
        await asyncio.sleep(10)
        await client.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.listening, name='modzbott.tk'))
        await asyncio.sleep(10)
        await client.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.listening, name='m/help'))
        await asyncio.sleep(10)

@client.event
async def on_message(message):
    if message.content.startswith('m/help'):
        if message.author.bot:
            return
        else:
            helpembed = discord.Embed(
              title="m/help", description="You can find help and support here:", color=discord.Color.purple())
            helpembed.add_field(name="Github repository", value="A full list of commands can be found here: https://github.com/MindOfModz/ModzBott")
            helpembed.add_field(name="Discord Bot List", value="Find the bot page here on top.gg: https://top.gg/bot/709030261605793803")
            helpembed.add_field(name="Support Server", value="Join the support server here for further support: https://discord.gg/nzEnYtZ")
            await message.author.send(embed = helpembed)
            helpoutput = await message.channel.send('Help was sent to your DMs.')
            await asyncio.sleep(8)
            await helpoutput.delete()
    elif message.content.startswith('m/flipcoin'):
        if message.author.bot:
            return
        else:
            choices = ['Heads!', 'Tails!']
            rancoin = random.choice(choices)
            choice = await message.channel.send(rancoin)

            await message.delete()
            await asyncio.sleep(10)

            await choice.delete()
    elif message.content.startswith('m/magicball'):
        if message.author.bot:
            return
        else:
            responses = [
                "It is certain.", "It is decidedly so.", "Without a doubt.",
                "Yes - definitely.", "You may rely on it.", "As I see it, yes.",
                "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.",
                "Reply hazy, try again.", "Ask again later.",
                "Better not tell you now.", "Cannot predict now.",
                "Concentrate and ask again.", "Don't count on it.",
                "My reply is no.", "My sources say no.", "Outlook not so good.",
                "Very doubtful."]
            response = random.choice(responses)
            output = await message.channel.send(response)

            await message.delete()
            await asyncio.sleep(12.5)

            await output.delete()
    elif message.content.startswith('m/invite'):
        if message.author.bot:
            return
        else:
            embed = discord.Embed(
            title='Invite me to your server.',
            description=
            '**Like what i can do? Invite me to your server!**\n\nhttps://discord.com/oauth2/authorize?client_id=709030261605793803&permissions=1476619382&scope=bot',
            colour=discord.Color.red())
            invitelink = await message.channel.send(embed=embed)

            await message.delete()
            await asyncio.sleep(13)

            await invitelink.delete()
    elif message.content.startswith('m/coolcheck'):
        if message.author.bot:
            return
        else:
            coolcheckchoice = [
            '0%', '1%', '2%', '3%', '4%', '5%', '6%', '7%', '8%', '9%', '10%',
            '11%', '12%', '13%', '14%', '15%', '16%', '17%', '18%', '19%',
            '20%', '21%', '22%', '23%', '24%', '25%', '26%', '27%', '28%',
            '29%', '30%', '31%', '32%', '33%', '34%', '35%', '36%', '37%',
            '38%', '39%', '40%', '41%', '42%', '43%', '44%', '45%', '46%',
            '47%', '48%', '49%', '50%', '51%', '52%', '53%', '54%', '55%',
            '56%', '57%', '58%', '59%', '60%', '61%', '62%', '63%', '64%',
            '65%', '66%', '67%', '68%', '69%', '70%', '71%', '72%', '73%',
            '74%', '75%', '76%', '77%', '78%', '79%', '80%', '81%', '82%',
            '83%', '84%', '85%', '86%', '87%', '88%', '89%', '90%', '91%',
            '92%', '93%', '94%', '95%', '96%', '97%', '98%', '99%', '100%',
            '101%'
        ]

            coolcheckrandomchoice = random.choice(coolcheckchoice)
            coolcheckoutput = await message.channel.send(
            f'You are {coolcheckrandomchoice} cool.')

            await message.delete()
            await asyncio.sleep(7.5)

            await coolcheckoutput.delete()
    elif message.content.startswith('m/servercount'):
        if message.author.bot:
            return
        else:
            servers = list(client.guilds)
            connected1 = await message.channel.send(
            f'Connected on {str(len(servers))} servers: ')
            

            await message.delete()
            await asyncio.sleep(10)
            await connected1.delete()
    elif message.content.startswith('m/serverlist'):
        if message.author.bot:
            return
        else:
            servers = list(client.guilds)
            connected2 = await message.channel.send('\n'.join(
            server.name for server in servers))
            connectedtest = await message.channel.send(servers)
            await message.delete()
            await asyncio.sleep(30)

            await connected2.delete()
    elif message.content.startswith('m/clear'):
      if message.author.bot:
        return
      else:
        clearamount = 101
        clearamountembed = 100
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        clearamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await clearamountembed1.delete()
        await message.channel.purge(limit=clearamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        clearamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await clearamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{clearamountembed} messages** from the channel!", color=discord.Color.green())
        clearamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await clearamountembed3.delete()
    elif message.content.startswith('m/1clear'):
      if message.author.bot:
          return
      else:
          oneamount = 2
          oneamountembed = 1
          embed1 = discord.Embed(
            title="Channel Cleaning.", description="Cleaning of channel is in progress.", color=0xffe705)
          oneamountembed1 = await message.channel.send(embed = embed1)
          await asyncio.sleep(0.13)
          await oneamountembed1.delete()
          await message.channel.purge(limit=oneamount)
          embed2 = discord.Embed(
            title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
          oneamountembed2 = await message.channel.send(embed = embed2)
          await asyncio.sleep(0.05)
          await oneamountembed2.delete()
          embed3 = discord.Embed(
            title="Channel Cleaning.", description=f"Successfully deleted **{oneamountembed} messages** from the channel!", color=discord.Color.green())
          oneamountembed3 = await message.channel.send(embed = embed3)
          await asyncio.sleep(13)
          await oneamountembed3.delete()
    elif message.content.startswith('m/2clear'):
      if message.author.bot:
        return
      else:
        twoamount = 3
        twoamountembed = 2
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        twoamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await twoamountembed1.delete()
        await message.channel.purge(limit=twoamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        twoamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.13)
        await twoamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{twoamountembed} messages** from the channel!", color=discord.Color.green())
        twoamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await twoamountembed3.delete()
    elif message.content.startswith('m/3clear'):
      if message.author.bot:
        return
      else:
        threeamount = 4
        threeamountembed = 3
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        threeamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await threeamountembed1.delete()
        await message.channel.purge(limit=threeamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        threeamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.13)
        await threeamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{threeamountembed} messages** from the channel!", color=discord.Color.green())
        threeamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await threeamountembed3.delete()
    elif message.content.startswith('m/4clear'):
      if message.author.bot:
        return
      else:
        fouramount = 5
        fouramountembed = 4
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        fouramountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await fouramountembed1.delete()
        await message.channel.purge(limit=fouramount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        fouramountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.13)
        await fouramountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{fouramountembed} messages** from the channel!", color=discord.Color.green())
        fouramountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await fouramountembed3.delete()
    elif message.content.startswith('m/5clear'):
      if message.author.bot:
        return
      else:
        fiveamount = 6
        fiveamountembed = 5
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        fiveamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await fiveamountembed1.delete()
        await message.channel.purge(limit=fiveamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        fiveamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await fiveamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{fiveamountembed} messages** from the channel!", color=discord.Color.green())
        fiveamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await fiveamountembed3.delete()
    elif message.content.startswith('m/6clear'):
      if message.author.bot:
        return
      else:
        sixamount = 7
        sixamountembed = 6
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        sixamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await sixamountembed1.delete()
        await message.channel.purge(limit=sixamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        sixamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await sixamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{sixamountembed} messages** from the channel!", color=discord.Color.green())
        sixamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await sixamountembed3.delete()
    elif message.content.startswith('m/7clear'):
      if message.author.bot:
        return
      else:
        sevenamount = 8
        sevenamountembed = 7
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        sevenamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await sevenamountembed1.delete()
        await message.channel.purge(limit=sevenamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        sevenamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await sevenamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{sevenamountembed} messages** from the channel!", color=discord.Color.green())
        sevenamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await sevenamountembed3.delete()
    elif message.content.startswith('m/8clear'):
      if message.author.bot:
        return
      else:
        eightamount = 9
        eightamountembed = 8
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        eightamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await eightamountembed1.delete()
        await message.channel.purge(limit=eightamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        eightamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await eightamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{eightamountembed} messages** from the channel!", color=discord.Color.green())
        eightamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await eightamountembed3.delete()
    elif message.content.startswith('m/9clear'):
      if message.author.bot:
        return
      else:
        nineamount = 10
        nineamountembed = 9
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        nineamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await nineamountembed1.delete()
        await message.channel.purge(limit=nineamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        nineamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await nineamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{nineamountembed} messages** from the channel!", color=discord.Color.green())
        nineamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await nineamountembed3.delete()
    elif message.content.startswith('m/10clear'):
      if message.author.bot:
        return
      else:
        tenamount = 11
        tenamountembed = 10
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        tenamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await tenamountembed1.delete()
        await message.channel.purge(limit=tenamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        tenamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await tenamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{tenamountembed} messages** from the channel!", color=discord.Color.green())
        tenamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await tenamountembed3.delete()
    elif message.content.startswith('m/11clear'):
      if message.author.bot:
        return
      else:
        elevenamount = 12
        elevenamountembed = 11
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        elevenamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await elevenamountembed1.delete()
        await message.channel.purge(limit=elevenamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        elevenamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await elevenamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{elevenamountembed} messages** from the channel!", color=discord.Color.green())
        elevenamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await elevenamountembed3.delete()
    elif message.content.startswith('m/12clear'):
      if message.author.bot:
        return
      else:
        twelveamount = 13
        twelveamountembed = 12
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        twelveamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await twelveamountembed1.delete()
        await message.channel.purge(limit=twelveamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        twelveamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await twelveamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{twelveamountembed} messages** from the channel!", color=discord.Color.green())
        twelveamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await twelveamountembed3.delete()
    elif message.content.startswith('m/13clear'):
      if message.author.bot:
        return
      else:
        thirteenamount = 14
        thirteenamountembed = 13
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        thirteenamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await thirteenamountembed1.delete()
        await message.channel.purge(limit=thirteenamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        thirteenamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await thirteenamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{thirteenamountembed} messages** from the channel!", color=discord.Color.green())
        thirteenamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await thirteenamountembed3.delete()
    elif message.content.startswith('m/7clear'):
      if message.author.bot:
        return
      else:
        fourteenamount = 15
        fourteenamountembed = 14
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        fourteenamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await fourteenamountembed1.delete()
        await message.channel.purge(limit=fourteenamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        fourteenamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await fourteenamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{fourteenamountembed} messages** from the channel!", color=discord.Color.green())
        fourteenamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await fourteenamountembed3.delete()
    elif message.content.startswith('m/15clear'):
      if message.author.bot:
        return
      else:
        fifteenamount = 16
        fifteenamountembed = 15
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        fifteenamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await fifteenamountembed1.delete()
        await message.channel.purge(limit=fifteenamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        fifteenamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await fifteenamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{fifteenamountembed} messages** from the channel!", color=discord.Color.green())
        fifteenamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await fifteenamountembed3.delete()
    elif message.content.startswith('m/16clear'):
      if message.author.bot:
        return
      else:
        sixteenamount = 17
        sixteenamountembed = 16
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        sixteenamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await sixteenamountembed1.delete()
        await message.channel.purge(limit=sixteenamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        sixteenamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await sixteenamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{sixteenamountembed} messages** from the channel!", color=discord.Color.green())
        sixteenamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await sixteenamountembed3.delete()
    elif message.content.startswith('m/17clear'):
      if message.author.bot:
        return
      else:
        seventeenamount = 18
        seventeenamountembed = 17
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        seventeenamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await seventeenamountembed1.delete()
        await message.channel.purge(limit=seventeenamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        seventeenamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await seventeenamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{seventeenamountembed} messages** from the channel!", color=discord.Color.green())
        eightamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await eightamountembed3.delete()
    elif message.content.startswith('m/18clear'):
      if message.author.bot:
        return
      else:
        eighteenamount = 19
        eighteenamountembed = 18
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        eighteenamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await eighteenamountembed1.delete()
        await message.channel.purge(limit=eighteenamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        eighteenamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await eighteenamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{eighteenamountembed} messages** from the channel!", color=discord.Color.green())
        eighteenamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await eighteenamountembed3.delete()
    elif message.content.startswith('m/19clear'):
      if message.author.bot:
        return
      else:
        nineteenamount = 20
        nineteenamountembed = 19
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        nineteenamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await nineteenamountembed1.delete()
        await message.channel.purge(limit=nineteenamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        nineteenamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await nineteenamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{nineteenamountembed} messages** from the channel!", color=discord.Color.green())
        nineteenamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await nineteenamountembed3.delete()
    elif message.content.startswith('m/20clear'):
      if message.author.bot:
        return
      else:
        twentyamount = 21
        twentyamountembed = 20
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        twentyamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await twentyamountembed1.delete()
        await message.channel.purge(limit=twentyamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        twentyamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await twentyamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{twentyamountembed} messages** from the channel!", color=discord.Color.green())
        twentyamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await twentyamountembed3.delete()
    elif message.content.startswith('m/21clear'):
      if message.author.bot:
        return
      else:
        twentyoneamount = 22
        twentyoneamountembed = 21
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        twentyoneamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await twentyoneamountembed1.delete()
        await message.channel.purge(limit=twentyoneamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        twentyoneamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await twentyoneamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{twentyoneamountembed} messages** from the channel!", color=discord.Color.green())
        twentyoneamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await twentyoneamountembed3.delete()
    elif message.content.startswith('m/22clear'):
      if message.author.bot:
        return
      else:
        twentytwoamount = 23
        twentytwoamountembed = 22
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        twentytwoamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await twentytwoamountembed1.delete()
        await message.channel.purge(limit=twentytwoamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        twentytwoamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await twentytwoamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{twentytwoamountembed} messages** from the channel!", color=discord.Color.green())
        twentytwoamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await twentytwoamountembed3.delete()
    elif message.content.startswith('m/23clear'):
      if message.author.bot:
        return
      else:
        twentythreeamount = 24
        twentythreeamountembed = 23
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        twentythreeamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await twentythreeamountembed1.delete()
        await message.channel.purge(limit=twentythreeamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        twentythreeamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await twentythreeamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{twentythreeamountembed} messages** from the channel!", color=discord.Color.green())
        twentythreeamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await twentythreeamountembed3.delete()
    elif message.content.startswith('m/24clear'):
      if message.author.bot:
        return
      else:
        twentyfouramount = 25
        twentyfouramountembed = 24
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        twentyfouramountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await twentyfouramountembed1.delete()
        await message.channel.purge(limit=twentyfouramount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        twentyfouramountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await twentyfouramountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{twentyfouramountembed} messages** from the channel!", color=discord.Color.green())
        twentyfouramountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await twentyfouramountembed3.delete()
    elif message.content.startswith('m/25clear'):
      if message.author.bot:
        return
      else:
        twentyfiveamount = 26
        twentyfiveamountembed = 25
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        twentyfiveamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await twentyfiveamountembed1.delete()
        await message.channel.purge(limit=twentyfiveamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        twentyfiveamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await twentyfiveamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{twentyfiveamountembed} messages** from the channel!", color=discord.Color.green())
        twentyfiveamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await twentyfiveamountembed3.delete()
    elif message.content.startswith('m/26clear'):
      if message.author.bot:
        return
      else:
        twentysixamount = 27
        twentysixamountembed = 26
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        twentysixamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await twentysixamountembed1.delete()
        await message.channel.purge(limit=twentysixamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        twentysixamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await twentysixamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{twentysixamountembed} messages** from the channel!", color=discord.Color.green())
        twentysixamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await twentysixamountembed3.delete()
    elif message.content.startswith('m/27clear'):
      if message.author.bot:
        return
      else:
        twentysevenamount = 28
        twentysevenamountembed = 27
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        twentysevenamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await twentysevenamountembed1.delete()
        await message.channel.purge(limit=twentysevenamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        twentysevenamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await twentysevenamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{twentysevenamountembed} messages** from the channel!", color=discord.Color.green())
        twentysevenamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await twentysevenamountembed3.delete()
    elif message.content.startswith('m/28clear'):
      if message.author.bot:
        return
      else:
        twentyeightamount = 29
        twentyeightamountembed = 28
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        twentyeightamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await twentyeightamountembed1.delete()
        await message.channel.purge(limit=twentyeightamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        twentyeightamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await twentyeightamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{twentyeightamountembed} messages** from the channel!", color=discord.Color.green())
        twentyeightamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await twentyeightamountembed3.delete()
    elif message.content.startswith('m/29clear'):
      if message.author.bot:
        return
      else:
        twentynineamount = 30
        twentynineamountembed = 29
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        twentynineamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await twentynineamountembed1.delete()
        await message.channel.purge(limit=twentynineamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        twentynineamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await twentynineamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{twentynineamountembed} messages** from the channel!", color=discord.Color.green())
        twentynineamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await twentynineamountembed3.delete()
    elif message.content.startswith('m/30clear'):
      if message.author.bot:
        return
      else:
        thirtyamount = 31
        thirtyamountembed = 30
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        thirtyamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await thirtyamountembed1.delete()
        await message.channel.purge(limit=thirtyamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        thirtyamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await thirtyamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{thirtyamountembed} messages** from the channel!", color=discord.Color.green())
        thirtyamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await thirtyamountembed3.delete()
    elif message.content.startswith('m/31clear'):
      if message.author.bot:
        return
      else:
        thirtyoneamount = 32
        thirtyoneamountembed = 31
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        thirtyoneamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await thirtyoneamountembed1.delete()
        await message.channel.purge(limit=thirtyoneamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        thirtyoneamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await thirtyoneamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{thirtyoneamountembed} messages** from the channel!", color=discord.Color.green())
        thirtyoneamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await thirtyoneamountembed3.delete()
    elif message.content.startswith('m/32clear'):
      if message.author.bot:
        return
      else:
        thirtytwoamount = 33
        thirtytwoamountembed = 32
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        thirtytwoamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await thirtytwoamountembed1.delete()
        await message.channel.purge(limit=thirtytwoamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        thirtytwoamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await thirtytwoamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{thirtytwoamountembed} messages** from the channel!", color=discord.Color.green())
        thirtytwoamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await thirtytwoamountembed3.delete()
    elif message.content.startswith('m/33clear'):
      if message.author.bot:
        return
      else:
        thirtythreeamount = 34
        thirtythreeamountembed = 33
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        thirtythreeamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await thirtythreeamountembed1.delete()
        await message.channel.purge(limit=thirtythreeamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        thirtythreeamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await thirtythreeamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{thirtythreeamountembed} messages** from the channel!", color=discord.Color.green())
        thirtythreeamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await thirtythreeamountembed3.delete()
    elif message.content.startswith('m/34clear'):
      if message.author.bot:
        return
      else:
        thirtyfouramount = 35
        thirtyfouramountembed = 34
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        thirtyfouramountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await thirtyfouramountembed1.delete()
        await message.channel.purge(limit=thirtyfouramount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        thirtyfouramountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await thirtyfouramountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{thirtyfouramountembed} messages** from the channel!", color=discord.Color.green())
        thirtyfouramountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await thirtyfouramountembed3.delete()
    elif message.content.startswith('m/35clear'):
      if message.author.bot:
        return
      else:
        thirtyfiveamount = 36
        thirtyfiveamountembed = 35
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        thirtyfiveamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await thirtyfiveamountembed1.delete()
        await message.channel.purge(limit=thirtyfiveamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        thirtyfiveamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await thirtyfiveamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{thirtyfiveamountembed} messages** from the channel!", color=discord.Color.green())
        thirtyfiveamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await thirtyfiveamountembed3.delete()
    elif message.content.startswith('m/36clear'):
      if message.author.bot:
        return
      else:
        thirtysixamount = 37
        thirtysixamountembed = 36
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        thirtysixamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await thirtysixamountembed1.delete()
        await message.channel.purge(limit=thirtysixamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        thirtysixamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await thirtysixamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{thirtysixamountembed} messages** from the channel!", color=discord.Color.green())
        thirtysixamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await thirtysixamountembed3.delete()
    elif message.content.startswith('m/37clear'):
      if message.author.bot:
        return
      else:
        thirtysevenamount = 38
        thirtysevenamountembed = 37
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        thirtysevenamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await thirtysevenamountembed1.delete()
        await message.channel.purge(limit=thirtysevenamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        thirtysevenamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await thirtysevenamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{thirtysevenamountembed} messages** from the channel!", color=discord.Color.green())
        thirtysevenamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await thirtysevenamountembed3.delete()
    elif message.content.startswith('m/38clear'):
      if message.author.bot:
        return
      else:
        thirtyeightamount = 39
        thirtyeightamountembed = 38
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        thirtyeightamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await thirtyeightamountembed1.delete()
        await message.channel.purge(limit=thirtyeightamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        thirtyeightamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await thirtyeightamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{thirtyeightamountembed} messages** from the channel!", color=discord.Color.green())
        thirtyeightamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await thirtyeightamountembed3.delete()
    elif message.content.startswith('m/39clear'):
      if message.author.bot:
        return
      else:
        thirtynineamount = 40
        thirtynineamountembed = 39
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        thirtynineamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await thirtynineamountembed1.delete()
        await message.channel.purge(limit=thirtynineamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        thirtynineamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await thirtynineamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{thirtynineamountembed} messages** from the channel!", color=discord.Color.green())
        thirtynineamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await thirtynineamountembed3.delete()
    elif message.content.startswith('m/40clear'):
      if message.author.bot:
        return
      else:
        fourtyamount = 41
        fourtyamountembed = 40
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        fourtyamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await fourtyamountembed1.delete()
        await message.channel.purge(limit=fourtyamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        fourtyamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await fourtyamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{fourtyamountembed} messages** from the channel!", color=discord.Color.green())
        fourtyamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await fourtyamountembed3.delete()
    elif message.content.startswith('m/41clear'):
      if message.author.bot:
        return
      else:
        fourtyoneamount = 42
        fourtyoneamountembed = 41
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        fourtyoneamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await fourtyoneamountembed1.delete()
        await message.channel.purge(limit=fourtyoneamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        fourtyoneamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await fourtyoneamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{fourtyoneamountembed} messages** from the channel!", color=discord.Color.green())
        fourtyoneamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await fourtyoneamountembed3.delete()
    elif message.content.startswith('m/42clear'):
      if message.author.bot:
        return
      else:
        fourtytwoamount = 43
        fourtytwoamountembed = 41
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        fourtytwoamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await fourtytwoamountembed1.delete()
        await message.channel.purge(limit=fourtytwoamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        fourtytwoamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await fourtytwoamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{fourtytwoamountembed} messages** from the channel!", color=discord.Color.green())
        fourtytwoamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await fourtytwoamountembed3.delete()
    elif message.content.startswith('m/43clear'):
      if message.author.bot:
        return
      else:
        fourtythreeamount = 44
        fourtythreeamountembed = 43
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        fourtythreeamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await fourtythreeamountembed1.delete()
        await message.channel.purge(limit=fourtythreeamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        fourtythreeamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await fourtythreeamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{fourtythreeamountembed} messages** from the channel!", color=discord.Color.green())
        fourtythreeamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await fourtythreeamountembed3.delete()
    elif message.content.startswith('m/44clear'):
      if message.author.bot:
        return
      else:
        fourtyfouramount = 45
        fourtyfouramountembed = 44
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        fourtyfouramountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await fourtyfouramountembed1.delete()
        await message.channel.purge(limit=fourtyfouramount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        fourtyfouramountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await fourtyfouramountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{fourtyfouramountembed} messages** from the channel!", color=discord.Color.green())
        fourtyfouramountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await fourtyfouramountembed3.delete()
    elif message.content.startswith('m/45clear'):
      if message.author.bot:
        return
      else:
        fourtyfiveamount = 46
        fourtyfiveamountembed = 45
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        fourtyfiveamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await fourtyfiveamountembed1.delete()
        await message.channel.purge(limit=fourtyfiveamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        fourtyfiveamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await fourtyfiveamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{fourtyfiveamountembed} messages** from the channel!", color=discord.Color.green())
        fourtyfiveamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await fourtyfiveamountembed3.delete()
    elif message.content.startswith('m/46clear'):
      if message.author.bot:
        return
      else:
        fourtysixamount = 47
        fourtysixamountembed = 46
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        fourtysixamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await fourtysixamountembed1.delete()
        await message.channel.purge(limit=fourtysixamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        fourtysixamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await fourtysixamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{fourtysixamountembed} messages** from the channel!", color=discord.Color.green())
        fourtysixamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await fourtysixamountembed3.delete()
    elif message.content.startswith('m/47clear'):
      if message.author.bot:
        return
      else:
        fourtysevenamount = 48
        fourtysevenamountembed = 47
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        fourtysevenamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await fourtysevenamountembed1.delete()
        await message.channel.purge(limit=fourtysevenamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        fourtysevenamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await fourtysevenamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{fourtysevenamountembed} messages** from the channel!", color=discord.Color.green())
        fourtysevenamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await fourtysevenamountembed3.delete()
    elif message.content.startswith('m/48clear'):
      if message.author.bot:
        return
      else:
        fourtyeightamount = 49
        fourtyeightamountembed = 48
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        fourtyeightamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await fourtyeightamountembed1.delete()
        await message.channel.purge(limit=fourtyeightamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        fourtyeightamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await fourtyeightamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{fourtyeightamountembed} messages** from the channel!", color=discord.Color.green())
        fourtyeightamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await fourtyeightamountembed3.delete()
    elif message.content.startswith('m/49clear'):
      if message.author.bot:
        return
      else:
        fourtynineamount = 50
        fourtynineamountembed = 49
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        fourtynineamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await fourtynineamountembed1.delete()
        await message.channel.purge(limit=fourtynineamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        fourtynineamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await fourtynineamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{fourtynineamountembed} messages** from the channel!", color=discord.Color.green())
        fourtynineamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await fourtynineamountembed3.delete()
    elif message.content.startswith('m/50clear'):
      if message.author.bot:
        return
      else:
        fiftyamount = 51
        fiftyamountembed = 50
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        fiftyamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await fiftyamountembed1.delete()
        await message.channel.purge(limit=fiftyamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        fiftyamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await fiftyamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{fiftyamountembed} messages** from the channel!", color=discord.Color.green())
        fiftyamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await fiftyamountembed3.delete()
    elif message.content.startswith('m/51clear'):
      if message.author.bot:
        return
      else:
        fiftyoneamount = 51
        fiftyoneamountembed = 50
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        fiftyoneamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await fiftyoneamountembed1.delete()
        await message.channel.purge(limit=fiftyoneamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        fiftyoneamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await fiftyoneamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{fiftyoneamountembed} messages** from the channel!", color=discord.Color.green())
        fiftyoneamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await fiftyoneamountembed3.delete()
    elif message.content.startswith('m/52clear'):
      if message.author.bot:
        return
      else:
        fiftytwoamount = 53
        fiftytwoamountembed = 52
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        fiftytwoamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await fiftytwoamountembed1.delete()
        await message.channel.purge(limit=fiftytwoamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        fiftytwoamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await fiftytwoamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{fiftytwoamountembed} messages** from the channel!", color=discord.Color.green())
        fiftytwoamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await fiftytwoamountembed3.delete()
    elif message.content.startswith('m/53clear'):
      if message.author.bot:
        return
      else:
        fiftythreeamount = 54
        fiftythreeamountembed = 53
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        fiftythreeamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await fiftythreeamountembed1.delete()
        await message.channel.purge(limit=fiftythreeamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        fiftythreeamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await fiftythreeamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{fiftythreeamountembed} messages** from the channel!", color=discord.Color.green())
        fiftythreeamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await fiftythreeamountembed3.delete()
    elif message.content.startswith('m/54clear'):
      if message.author.bot:
        return
      else:
        fiftyfouramount = 55
        fiftyfouramountembed = 54
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        fiftyfouramountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await fiftyfouramountembed1.delete()
        await message.channel.purge(limit=fiftyfouramount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        fiftyfouramountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await fiftyfouramountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{fiftyfouramountembed} messages** from the channel!", color=discord.Color.green())
        fiftyfouramountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await fiftyfouramountembed3.delete()
    elif message.content.startswith('m/55clear'):
      if message.author.bot:
        return
      else:
        fiftyfiveamount = 56
        fiftyfiveamountembed = 55
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        fiftyfiveamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await fiftyfiveamountembed1.delete()
        await message.channel.purge(limit=fiftyfiveamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        fiftyfiveamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await fiftyfiveamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{fiftyfiveamountembed} messages** from the channel!", color=discord.Color.green())
        fiftyfiveamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await fiftyfiveamountembed3.delete()
    elif message.content.startswith('m/56clear'):
      if message.author.bot:
        return
      else:
        fiftysixamount = 57
        fiftysixamountembed = 56
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        fiftysixamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await fiftysixamountembed1.delete()
        await message.channel.purge(limit=fiftysixamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        fiftysixamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await fiftysixamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{fiftysixamountembed} messages** from the channel!", color=discord.Color.green())
        fiftysixamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await fiftysixamountembed3.delete()
    elif message.content.startswith('m/57clear'):
      if message.author.bot:
        return
      else:
        fiftysevenamount = 58
        fiftysevenamountembed = 57
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        fiftysevenamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await fiftysevenamountembed1.delete()
        await message.channel.purge(limit=fiftysevenamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        fiftysevenamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await fiftysevenamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{fiftysevenamountembed} messages** from the channel!", color=discord.Color.green())
        fiftysevenamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await fiftysevenamountembed3.delete()
    elif message.content.startswith('m/58clear'):
      if message.author.bot:
        return
      else:
        fiftyeightamount = 59
        fiftyeightamountembed = 58
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        fiftyeightamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await fiftyeightamountembed1.delete()
        await message.channel.purge(limit=fiftyeightamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        fiftyeightamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await fiftyeightamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{fiftyeightamountembed} messages** from the channel!", color=discord.Color.green())
        fiftyeightamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await fiftyeightamountembed3.delete()
    elif message.content.startswith('m/59clear'):
      if message.author.bot:
        return
      else:
        fiftynineamount = 60
        fiftynineamountembed = 59
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        fiftynineamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await fiftynineamountembed1.delete()
        await message.channel.purge(limit=fiftynineamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        fiftynineamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await fiftynineamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{fiftynineamountembed} messages** from the channel!", color=discord.Color.green())
        fiftynineamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await fiftynineamountembed3.delete()
    elif message.content.startswith('m/60clear'):
      if message.author.bot:
        return
      else:
        sixtyamount = 61
        sixtyamountembed = 60
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        sixtyamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await sixtyamountembed1.delete()
        await message.channel.purge(limit=sixtyamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        sixtyamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await sixtyamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{sixtyamountembed} messages** from the channel!", color=discord.Color.green())
        sixtyamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await sixtyamountembed3.delete()
    elif message.content.startswith('m/61clear'):
      if message.author.bot:
        return
      else:
        sixtyoneamount = 62
        sixtyoneamountembed = 61
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        sixtyoneamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await sixtyoneamountembed1.delete()
        await message.channel.purge(limit=sixtyoneamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        sixtyoneamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await sixtyoneamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{sixtyoneamountembed} messages** from the channel!", color=discord.Color.green())
        sixtyoneamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await sixtyoneamountembed3.delete()
    elif message.content.startswith('m/62clear'):
      if message.author.bot:
        return
      else:
        sixtytwoamount = 63
        sixtytwoamountembed = 62
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        sixtytwoamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await sixtytwoamountembed1.delete()
        await message.channel.purge(limit=sixtytwoamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        sixtytwoamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await sixtytwoamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{sixtytwoamountembed} messages** from the channel!", color=discord.Color.green())
        sixtytwoamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await sixtytwoamountembed3.delete()
    elif message.content.startswith('m/63clear'):
      if message.author.bot:
        return
      else:
        sixtythreeamount = 64
        sixtythreeamountembed = 63
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        sixtythreeamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await sixtythreeamountembed1.delete()
        await message.channel.purge(limit=sixtythreeamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        sixtythreeamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await sixtythreeamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{sixtythreeamountembed} messages** from the channel!", color=discord.Color.green())
        sixtythreeamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await sixtythreeamountembed3.delete()
    elif message.content.startswith('m/64clear'):
      if message.author.bot:
        return
      else:
        sixtyfouramount = 65
        sixtyfouramountembed = 64
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        sixtyfouramountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await sixtyfouramountembed1.delete()
        await message.channel.purge(limit=sixtyfouramount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        sixtyfouramountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await sixtyfouramountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{sixtyfouramountembed} messages** from the channel!", color=discord.Color.green())
        sixtyfouramountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await sixtyfouramountembed3.delete()
    elif message.content.startswith('m/65clear'):
      if message.author.bot:
        return
      else:
        sixtyfiveamount = 66
        sixtyfiveamountembed = 65
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        sixtyfiveamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await sixtyfiveamountembed1.delete()
        await message.channel.purge(limit=sixtyfiveamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        sixtyfiveamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await sixtyfiveamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{sixtyfiveamountembed} messages** from the channel!", color=discord.Color.green())
        sixtyfiveamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await sixtyfiveamountembed3.delete()
    elif message.content.startswith('m/66clear'):
      if message.author.bot:
        return
      else:
        sixtysixamount = 67
        sixtysixamountembed = 66
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        sixtysixamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await sixtysixamountembed1.delete()
        await message.channel.purge(limit=sixtysixamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        sixtysixamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await sixtysixamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{sixtysixamountembed} messages** from the channel!", color=discord.Color.green())
        sixtysixamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await sixtysixamountembed3.delete()
    elif message.content.startswith('m/67clear'):
      if message.author.bot:
        return
      else:
        sixtysevenamount = 68
        sixtysevenamountembed = 67
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        sixtysevenamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await sixtysevenamountembed1.delete()
        await message.channel.purge(limit=sixtysevenamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        sixtysevenamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await sixtysevenamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{sixtysevenamountembed} messages** from the channel!", color=discord.Color.green())
        sixtysevenamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await sixtysevenamountembed3.delete()
    elif message.content.startswith('m/68clear'):
      if message.author.bot:
        return
      else:
        sixtyeightamount = 69
        sixtyeightamountembed = 68
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        sixtyeightamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await sixtyeightamountembed1.delete()
        await message.channel.purge(limit=sixtyeightamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        sixtyeightamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await sixtyeightamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{sixtyeightamountembed} messages** from the channel!", color=discord.Color.green())
        sixtyeightamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await sixtyeightamountembed3.delete()
    elif message.content.startswith('m/69clear'):
      if message.author.bot:
        return
      else:
        sixtynineamount = 70
        sixtynineamountembed = 69
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        sixtynineamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await sixtynineamountembed1.delete()
        await message.channel.purge(limit=sixtynineamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        sixtynineamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await sixtynineamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{sixtynineamountembed} messages** from the channel!", color=discord.Color.green())
        sixtynineamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await sixtynineamountembed3.delete()
    elif message.content.startswith('m/70clear'):
      if message.author.bot:
        return
      else:
        seventyamount = 71
        seventyamountembed = 70
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        seventyamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await seventyamountembed1.delete()
        await message.channel.purge(limit=seventyamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        seventyamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await seventyamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{seventyamountembed} messages** from the channel!", color=discord.Color.green())
        seventyamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await seventyamountembed3.delete()
    elif message.content.startswith('m/71clear'):
      if message.author.bot:
        return
      else:
        seventyoneamount = 72
        seventyoneamountembed = 71
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        seventyoneamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await seventyoneamountembed1.delete()
        await message.channel.purge(limit=seventyoneamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        seventyoneamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await seventyoneamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{seventyoneamountembed} messages** from the channel!", color=discord.Color.green())
        seventyoneamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await seventyoneamountembed3.delete()
    elif message.content.startswith('m/72clear'):
      if message.author.bot:
        return
      else:
        seventytwoamount = 73
        seventytwoamountembed = 72
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        seventytwoamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await seventytwoamountembed1.delete()
        await message.channel.purge(limit=seventytwoamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        seventytwoamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await seventytwoamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{seventytwoamountembed} messages** from the channel!", color=discord.Color.green())
        seventytwoamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await seventytwoamountembed3.delete()
    elif message.content.startswith('m/73clear'):
      if message.author.bot:
        return
      else:
        seventythreeamount = 74
        seventythreeamountembed = 73
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        seventythreeamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await seventythreeamountembed1.delete()
        await message.channel.purge(limit=seventythreeamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        seventythreeamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await seventythreeamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{seventythreeamountembed} messages** from the channel!", color=discord.Color.green())
        seventythreeamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await seventythreeamountembed3.delete()
    elif message.content.startswith('m/74clear'):
      if message.author.bot:
        return
      else:
        seventyfouramount = 75
        seventyfouramountembed = 74
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        seventyfouramountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await seventyfouramountembed1.delete()
        await message.channel.purge(limit=seventyfouramount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        seventyfouramountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await seventyfouramountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{seventyfouramountembed} messages** from the channel!", color=discord.Color.green())
        seventyfouramountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await seventyfouramountembed3.delete()
    elif message.content.startswith('m/75clear'):
      if message.author.bot:
        return
      else:
        seventyfiveamount = 76
        seventyfiveamountembed = 75
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        seventyfiveamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await seventyfiveamountembed1.delete()
        await message.channel.purge(limit=seventyfiveamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        seventyfiveamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await seventyfiveamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{seventyfiveamountembed} messages** from the channel!", color=discord.Color.green())
        seventyfiveamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await seventyfiveamountembed3.delete()
    elif message.content.startswith('m/76clear'):
      if message.author.bot:
        return
      else:
        seventysixamount = 77
        seventysixamountembed = 76
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        seventysixamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await seventysixamountembed1.delete()
        await message.channel.purge(limit=seventysixamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        seventysixamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await seventysixamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{seventysixamountembed} messages** from the channel!", color=discord.Color.green())
        seventysixamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await seventysixamountembed3.delete()
    elif message.content.startswith('m/77clear'):
      if message.author.bot:
        return
      else:
        seventysevenamount = 78
        seventysevenamountembed = 77
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        seventysevenamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await seventysevenamountembed1.delete()
        await message.channel.purge(limit=seventysevenamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        seventysevenamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await seventysevenamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{seventysevenamountembed} messages** from the channel!", color=discord.Color.green())
        seventysevenamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await seventysevenamountembed3.delete()
    elif message.content.startswith('m/78clear'):
      if message.author.bot:
        return
      else:
        seventyeightamount = 79
        seventyeightamountembed = 78
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        seventyeightamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await seventyeightamountembed1.delete()
        await message.channel.purge(limit=seventyeightamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        seventyeightamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await seventyeightamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{seventyeightamountembed} messages** from the channel!", color=discord.Color.green())
        seventyeightamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await seventyeightamountembed3.delete()
    elif message.content.startswith('m/79clear'):
      if message.author.bot:
        return
      else:
        seventynineamount = 80
        seventynineamountembed = 79
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        seventynineamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await seventynineamountembed1.delete()
        await message.channel.purge(limit=seventynineamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        seventynineamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await seventynineamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{seventynineamountembed} messages** from the channel!", color=discord.Color.green())
        seventynineamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await seventynineamountembed3.delete()
    elif message.content.startswith('m/80clear'):
      if message.author.bot:
        return
      else:
        eightyamount = 81
        eightyamountembed = 80
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        eightyamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await eightyamountembed1.delete()
        await message.channel.purge(limit=eightyamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        eightyamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await eightyamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{eightyamountembed} messages** from the channel!", color=discord.Color.green())
        eightyamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await eightyamountembed3.delete()
    elif message.content.startswith('m/81clear'):
      if message.author.bot:
        return
      else:
        eightyoneamount = 82
        eightyoneamountembed = 81
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        eightyoneamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await eightyoneamountembed1.delete()
        await message.channel.purge(limit=eightyoneamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        eightyoneamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await eightyoneamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{eightyoneamountembed} messages** from the channel!", color=discord.Color.green())
        eightyoneamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await eightyoneamountembed3.delete()
    elif message.content.startswith('m/82clear'):
      if message.author.bot:
        return
      else:
        eightytwoamount = 83
        eightytwoamountembed = 82
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        eightytwoamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await eightytwoamountembed1.delete()
        await message.channel.purge(limit=eightytwoamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        eightytwoamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await eightytwoamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{eightytwoamountembed} messages** from the channel!", color=discord.Color.green())
        eightytwoamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await eightytwoamountembed3.delete()
    elif message.content.startswith('m/83clear'):
      if message.author.bot:
        return
      else:
        eightythreeamount = 84
        eightythreeamountembed = 83
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        eightythreeamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await eightythreeamountembed1.delete()
        await message.channel.purge(limit=eightythreeamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        eightythreeamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await eightythreeamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{eightythreeamountembed} messages** from the channel!", color=discord.Color.green())
        eightythreeamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await eightythreeamountembed3.delete()
    elif message.content.startswith('m/84clear'):
      if message.author.bot:
        return
      else:
        eightyfouramount = 85
        eightyfouramountembed = 84
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        eightyfouramountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await eightyfouramountembed1.delete()
        await message.channel.purge(limit=eightyfouramount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        eightyfouramountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await eightyfouramountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{eightyfouramountembed} messages** from the channel!", color=discord.Color.green())
        eightyfouramountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await eightyfouramountembed3.delete()
    elif message.content.startswith('m/85clear'):
      if message.author.bot:
        return
      else:
        eightyfiveamount = 86
        eightyfiveamountembed = 85
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        eightyfiveamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await eightyfiveamountembed1.delete()
        await message.channel.purge(limit=eightyfiveamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        eightyfiveamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await eightyfiveamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{eightyfiveamountembed} messages** from the channel!", color=discord.Color.green())
        eightyfiveamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await eightyfiveamountembed3.delete()
    elif message.content.startswith('m/86clear'):
      if message.author.bot:
        return
      else:
        eightysixamount = 87
        eightysixamountembed = 86
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        eightysixamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await eightysixamountembed1.delete()
        await message.channel.purge(limit=eightysixamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        eightysixamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await eightysixamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{eightysixamountembed} messages** from the channel!", color=discord.Color.green())
        eightysixamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await eightysixamountembed3.delete()
    elif message.content.startswith('m/87clear'):
      if message.author.bot:
        return
      else:
        eightysevenamount = 88
        eightysevenamountembed = 87
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        eightysevenamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await eightysevenamountembed1.delete()
        await message.channel.purge(limit=eightysevenamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        eightysevenamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await eightysevenamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{eightysevenamountembed} messages** from the channel!", color=discord.Color.green())
        eightysevenamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await eightysevenamountembed3.delete()
    elif message.content.startswith('m/88clear'):
      if message.author.bot:
        return
      else:
        eightyeightamount = 89
        eightyeightamountembed = 88
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        eightyeightamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await eightyeightamountembed1.delete()
        await message.channel.purge(limit=eightyeightamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        eightyeightamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await eightyeightamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{eightyeightamountembed} messages** from the channel!", color=discord.Color.green())
        eightyeightamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await eightyeightamountembed3.delete()
    elif message.content.startswith('m/89clear'):
      if message.author.bot:
        return
      else:
        eightynineamount = 90
        eightynineamountembed = 89
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        eightynineamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await eightynineamountembed1.delete()
        await message.channel.purge(limit=eightynineamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        eightynineamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await eightynineamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{eightynineamountembed} messages** from the channel!", color=discord.Color.green())
        eightynineamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await eightynineamountembed3.delete()
    elif message.content.startswith('m/90clear'):
      if message.author.bot:
        return
      else:
        ninetyamount = 91
        ninetyamountembed = 90
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        ninetyamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await ninetyamountembed1.delete()
        await message.channel.purge(limit=ninetyamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        ninetyamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await ninetyamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{ninetyamountembed} messages** from the channel!", color=discord.Color.green())
        ninetyamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await ninetyamountembed3.delete()
    elif message.content.startswith('m/91clear'):
      if message.author.bot:
        return
      else:
        ninetyoneamount = 92
        ninetyoneamountembed = 91
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        ninetyoneamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await ninetyoneamountembed1.delete()
        await message.channel.purge(limit=ninetyoneamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        ninetyoneamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await ninetyoneamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{ninetyoneamountembed} messages** from the channel!", color=discord.Color.green())
        ninetyoneamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await ninetyoneamountembed3.delete()
    elif message.content.startswith('m/92clear'):
      if message.author.bot:
        return
      else:
        ninetytwoamount = 93
        ninetytwoamountembed = 92
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        ninetytwoamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await ninetytwoamountembed1.delete()
        await message.channel.purge(limit=ninetytwoamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        ninetytwoamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await ninetytwoamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{ninetytwoamountembed} messages** from the channel!", color=discord.Color.green())
        ninetytwoamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await ninetytwoamountembed3.delete()
    elif message.content.startswith('m/93clear'):
      if message.author.bot:
        return
      else:
        ninetythreeamount = 94
        ninetythreeamountembed = 93
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        ninetythreeamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await ninetythreeamountembed1.delete()
        await message.channel.purge(limit=ninetythreeamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        ninetythreeamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await ninetythreeamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{ninetythreeamountembed} messages** from the channel!", color=discord.Color.green())
        ninetythreeamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await ninetythreeamountembed3.delete()
    elif message.content.startswith('m/94clear'):
      if message.author.bot:
        return
      else:
        ninetyfouramount = 95
        ninetyfouramountembed = 94
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        ninetyfouramountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await ninetyfouramountembed1.delete()
        await message.channel.purge(limit=ninetyfouramount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        ninetyfouramountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await ninetyfouramountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{ninetyfouramountembed} messages** from the channel!", color=discord.Color.green())
        ninetyfouramountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await ninetyfouramountembed3.delete()
    elif message.content.startswith('m/95clear'):
      if message.author.bot:
        return
      else:
        ninetyfiveamount = 96
        ninetyfiveamountembed = 95
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        ninetyfiveamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await ninetyfiveamountembed1.delete()
        await message.channel.purge(limit=ninetyfiveamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        ninetyfiveamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await ninetyfiveamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{ninetyfiveamountembed} messages** from the channel!", color=discord.Color.green())
        ninetyfiveamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await ninetyfiveamountembed3.delete()
    elif message.content.startswith('m/96clear'):
      if message.author.bot:
        return
      else:
        ninetysixamount = 97
        ninetysixamountembed = 96
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        ninetysixamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await ninetysixamountembed1.delete()
        await message.channel.purge(limit=ninetysixamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        ninetysixamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await ninetysixamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{ninetysixamountembed} messages** from the channel!", color=discord.Color.green())
        ninetysixamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await ninetysixamountembed3.delete()
    elif message.content.startswith('m/97clear'):
      if message.author.bot:
        return
      else:
        ninetysevenamount = 98
        ninetysevenamountembed = 97
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        ninetysevenamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await ninetysevenamountembed1.delete()
        await message.channel.purge(limit=ninetysevenamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        ninetysevenamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await ninetysevenamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{ninetysevenamountembed} messages** from the channel!", color=discord.Color.green())
        ninetysevenamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await ninetysevenamountembed3.delete()
    elif message.content.startswith('m/98clear'):
      if message.author.bot:
        return
      else:
        ninetyeightamount = 99
        ninetyeightamountembed = 98
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        ninetyeightamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await ninetyeightamountembed1.delete()
        await message.channel.purge(limit=ninetyeightamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        ninetyeightamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await ninetyeightamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{ninetyeightamountembed} messages** from the channel!", color=discord.Color.green())
        ninetyeightamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await ninetyeightamountembed3.delete()
    elif message.content.startswith('m/99clear'):
      if message.author.bot:
        return
      else:
        ninetynineamount = 100
        ninetynineamountembed = 99
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        ninetynineamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await ninetynineamountembed1.delete()
        await message.channel.purge(limit=ninetynineamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        ninetynineamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await ninetynineamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{ninetynineamountembed} messages** from the channel!", color=discord.Color.green())
        ninetynineamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await ninetynineamountembed3.delete()
    elif message.content.startswith('m/100clear'):
      if message.author.bot:
        return
      else:
        onehundredamount = 101
        onehundredamountembed = 100
        embed1 = discord.Embed(
          title="Channel Cleaning.", description="Cleaning of channel in progress.", color=0xffe705)
        onehundredamountembed1 = await message.channel.send(embed = embed1)
        await asyncio.sleep(0.18)
        await onehundredamountembed1.delete()
        await message.channel.purge(limit=onehundredamount)
        embed2 = discord.Embed(
          title="Channel Cleaning.", description="Finalising clean.", color=0xffe705)
        onehundredamountembed2 = await message.channel.send(embed = embed2)
        await asyncio.sleep(0.22)
        await onehundredamountembed2.delete()
        embed3 = discord.Embed(
          title="Channel Cleaning.", description=f"Successfully deleted **{onehundredamountembed} messages** from the channel!", color=discord.Color.green())
        onehundredamountembed3 = await message.channel.send(embed = embed3)
        await asyncio.sleep(13)
        await onehundredamountembed3.delete()
    elif message.content.startswith('m/qpoll'):
        await message.add_reaction('❌')
        await message.add_reaction('✔️')
        await message.add_reaction('❓')
        await message.delete()
# to be added (multiple choice poll)
#(m/mulpoll)
#
    elif message.content.startswith('m/work'):
      if message.author.bot:
        return
      else:
        workrandomchoice1 = discord.Embed(
          title=f"Work. **({message.author})**", description="You decided to work at a simple fish and chips shop. You earned $54.", color=discord.Color.green())
        workrandomchoice2 = discord.Embed(
          title=f"Work. **({message.author})**", description="You got promoted as a lead developer at Microsoft. You earned $273.", color=discord.Color.green())
        workrandomchoice3 = discord.Embed(
          title=f"Work. **({message.author})**", description="You deliver a sack of potatoes to a rich man and he gives you a large tip. Your recieve $161.", color=discord.Color.green())
        workrandomchoice4 = discord.Embed(
          title=f"Work. **({message.author})**", description="You work as a beaver analyst and earn $164.", color=discord.Color.green())
        workrandomchoice5 = discord.Embed(
          title=f"Work. **({message.author})**", description="You got hired to be a whiteboard marker salesperson and earn $76.", color=discord.Color.green())
        workrandomchoice6 = discord.Embed(
          title=f"Work. **({message.author})**", description="You start a facebook live channel and become huge. You earn $328.", color=discord.Color.green())
        workrandomchoice7 = discord.Embed(
          title=f"Work. **({message.author})**", description="You work as a penguinologist and earn $240.", color = discord.Color.green())
        workrandomchoice8 = discord.Embed(
          title=f"Work. **({message.author})**", description="You became a blacksmith in far lands and earned $4.", color=discord.Color.green())
        workrandomchoice9 = discord.Embed(
          title=f"Work. **({message.author})**", description="You become an experienced bra fitter and earn $109.", color=discord.Color.green())
        workrandomchoice10 = discord.Embed(
          title=f"Work. **({message.author})**", description="You were featured in a TV show and earned $613.", color=discord.Color.green())
        workrandomchoice11 = discord.Embed(
          title=f"Work. **({message.author})**", description="You become a cinema screen cleaner and earn $110.", color=discord.Color.green())
        workrandomchoice12 = discord.Embed(
          title=f"Work. **({message.author})**", description="You battled and earned $39.", color=discord.Color.green())
        workrandomchoice13 = discord.Embed(
          title=f"Work. **({message.author})**", description="You worked at the busiest market in the world and earned $596 from selling apples.", color=discord.Color.green())
        workrandomchoice14 = discord.Embed(
          title=f'Work. **({message.author})**',
          description='You get lead manager at Walmart. You earn $32.',
          color=discord.Color.green())
        workrandomchoice15 = discord.Embed(
          title=f'Work. **({message.author})**',
          description='You become a ROBLOX developer and earn $103.',
          color=discord.Color.green())
        workrandomchoice16 = discord.Embed(
          title=f"Work. **({message.author})**",
          description="You find a dinosaur in a field and breed them 24/7. You earn $785.",
          color = discord.Color.green())
        workrandomchoice17 = discord.Embed(
          title=f"Work. **({message.author})**",
          description="You built one of the floors of the empire state. You earn $1408.",
          color=discord.Color.green())
        workrandomchoice18 = discord.Embed(
          title=f"Work. **({message.author})**",
          description="You sign a petition to shut down some of the most popular games in the world and earn $3.",
          color=discord.Color.green())
        workrandomchoiceoutput = random.choice([workrandomchoice1, workrandomchoice2, workrandomchoice3, workrandomchoice4, workrandomchoice5, workrandomchoice6, workrandomchoice7, workrandomchoice8, workrandomchoice9, workrandomchoice10, workrandomchoice11, workrandomchoice12, workrandomchoice13, workrandomchoice14, workrandomchoice15, workrandomchoice16, workrandomchoice17, workrandomchoice18])
        await message.channel.send(embed = workrandomchoiceoutput)
    elif message.content.startswith('m/ping'):
      pingoutput1 = await message.channel.send('Pong!')
      await asyncio.sleep(5)
      pingoutput2 = await message.channel.send(f'**Currect latency: **{client.latency}')
      await asyncio.sleep(10)
      await pingoutput1.delete()
      await pingoutput2.delete()
    elif message.content.startswith('m/setup'):
      channel = message.channel
      guild = message.guild
      await channel.send('I am about to make a simple channel setup. **Continue?** (y/n)')

      def check(m):
        return m.author == message.author

      msg = await client.wait_for('message', check=check)
      if msg.content == 'yes' or msg.content == 'y':
        yesembed = discord.Embed(
          title='Creating channels.',
          description='I am now creating channels. Please wait.',
          color=discord.Color.red())
        await message.channel.send(embed=yesembed)
        await asyncio.sleep(1)
        await guild.create_text_channel('general')
        await asyncio.sleep(1)
        await guild.create_text_channel('off-topic')
        await asyncio.sleep(1)
        await guild.create_text_channel('commands')
        await asyncio.sleep(1)
        await guild.create_text_channel('announcements')
        await asyncio.sleep(1)
        await guild.create_text_channel('self-promotion')
        await asyncio.sleep(1)
        await guild.create_text_channel('server-logs')
        await asyncio.sleep(1)
        await guild.create_text_channel('staff-chat')
        await asyncio.sleep(2)
        await message.channel.send('**Channels created!**')
        await message.channel.send('I can not make roles or other components as of yet. Please use m/help if you need more assistance.')
      elif msg.content == 'no' or msg.content == 'n':
        await message.channel.send('Cancelled!')
      else:
        await message.channel.send('Invalid.')
keep_alive()
client.run(token)
