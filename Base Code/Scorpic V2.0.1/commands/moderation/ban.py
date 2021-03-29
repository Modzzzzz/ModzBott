from discord.ext import commands
import discord

class ban(commands.Cog):
    def __init__(self, client):
        self.client = client

    # When the cog boots up on bot launch:
    # It will print 'Ban Cog registered.'

    @commands.Cog.listener()
    async def on_ready(self):
        print("Ban Cog registered.")

    # Information command for users to request support by using s!ban @user {reason}
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        embed = discord.Embed(
            title='Member Banned',
            description=f'**{member}** has been banned from the server by **{ctx.author}** for **{reason}**',
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)
    

def setup(client):
    client.add_cog(ban(client))
