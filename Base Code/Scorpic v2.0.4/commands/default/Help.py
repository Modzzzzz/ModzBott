from discord.ext import commands
import discord

class help(commands.Cog):
    def __init__(self, client):
        self.client = client

    # When the cog boots up on bot launch:
    # It will print 'Information Cog registered.'

    @commands.Cog.listener()
    async def on_ready(self):
        print("Help Cog registered.")

    # Help command for users to request support by using s!help
    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(title="Scorpic Support")
        embed.add_field(name='GitHub Repository:', value="https://github.com/MindOfModz/Scorpic\n\n**Top.GG Page:**\nComing soon!\n\n**Support Server:**\nhttps://discord.gg/8S3QQpzxZz", inline=True)
        embed.set_thumbnail(url="https://raw.githubusercontent.com/MindOfModz/Scorpic/master/overhaul/OtherFiles/favicons.png")
        await ctx.channel.send(embed=embed)

def setup(client):
    client.add_cog(help(client))
