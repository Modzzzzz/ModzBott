from discord.ext import commands
import discord

class serverinfo(commands.Cog):
    def __init__(self, client):
        self.client = client

    # When the cog boots up on bot launch:
    # It will print 'Invite Cog registered.'

    @commands.Cog.listener()
    async def on_ready(self):
        print("Server Info Cog registered.")

    # Invite command for users to server info by using s!serverinfo
    @commands.command()
    async def serverinfo(self, ctx):
        embed = discord.Embed(
            title=f'Server Info For {ctx.guild.name}',
            color=discord.Color.green()
        )
        embed.add_field(name='Member Count:', value=f"```{ctx.guild.member_count}```", inline=True)
        embed.add_field(name='Server Owner:', value=f'```{ctx.guild.owner}```', inline=True)
        embed.add_field(name='Server Name:', value=f'```{ctx.guild.name}```', inline=True)
        embed.add_field(name='Server ID:', value=f'```{ctx.guild.id}```')
        embed.set_thumbnail(url=f"{ctx.guild.icon_url}")
        await ctx.channel.send(embed=embed)

def setup(client):
    client.add_cog(serverinfo(client))
