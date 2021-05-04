from discord.ext import commands
import discord

class invite(commands.Cog):
    def __init__(self, client):
        self.client = client

    # When the cog boots up on bot launch:
    # It will print 'Invite Cog registered.'

    @commands.Cog.listener()
    async def on_ready(self):
        print("Invite Cog registered.")

    # Invite command for users to invite the bot to their servers by using s!invite
    @commands.command()
    async def invite(self, ctx):
        embed = discord.Embed(title="Invite Scorpic To Your Server:")
        embed.add_field(name='Invite Link:', value="https://discord.com/api/oauth2/authorize?client_id=823453957564530759&permissions=3187011254&scope=bot", inline=True)
        embed.set_thumbnail(url="https://raw.githubusercontent.com/MindOfModz/Scorpic/master/overhaul/OtherFiles/favicons.png")
        await ctx.channel.send(embed=embed)

def setup(client):
    client.add_cog(invite(client))
