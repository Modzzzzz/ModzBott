from discord.ext import commands
import discord

class information(commands.Cog):
    def __init__(self, client):
        self.client = client

    # When the cog boots up on bot launch:
    # It will print 'Information Cog registered.'

    @commands.Cog.listener()
    async def on_ready(self):
        print("Information Cog registered.")

    # Information command for users to request support by using s!help
    @commands.command()
    async def information(self, ctx):
        embed = discord.Embed(title="Bot Informaton:")
        embed.add_field(name="Bot Creator:", value="```Lewiss#0352```", inline=True)
        embed.add_field(name="Creation Date:", value="```22/03/2021```", inline=True)
        embed.add_field(name="Bot Language:", value="```discord.py```", inline=True)
        embed.add_field(name="Bot Shards:", value="```0```", inline=True)
        embed.add_field(name='Bot Version:', value="```v2.0.1```", inline=True)
        embed.set_thumbnail(url="https://raw.githubusercontent.com/MindOfModz/Scorpic/master/overhaul/OtherFiles/favicons.png")
        await ctx.channel.send(embed=embed)
    

def setup(client):
    client.add_cog(information(client))
