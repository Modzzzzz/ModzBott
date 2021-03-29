from discord.ext import commands
import discord

class kick(commands.Cog):
    def __init__(self, client):
        self.client = client

    # When the cog boots up on bot launch:
    # It will print 'Kick Cog registered.'

    @commands.Cog.listener()
    async def on_ready(self):
        print("Kick Cog registered.")

    # Information command for users to request support by using s!kick @user {reason}
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        embed = discord.Embed(
            title='Member Kicked',
            description=f'**{member}** has been kicked from the server by **{ctx.author}** for **{reason}**',
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)
    

def setup(client):
    client.add_cog(kick(client))
