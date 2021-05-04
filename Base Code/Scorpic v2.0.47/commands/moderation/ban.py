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
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        try:
            await member.ban(reason=reason)
            embed = discord.Embed(
                title='Member Banned',
                description=f'**{member}** has been banned from the server by **{ctx.author}** for **{reason}**',
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)
        # If bot does not have the permission
        except discord.Forbidden:
            errorembed = discord.Embed(
                title='Missing Permissions',
                description=':x: I need the **Ban Members** permission to ban members!',
                color=discord.Color.red()
            )
            await ctx.send(embed=errorembed)

    # If the user does not have the permission
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                title='Missing Permissions',
                description=f':x: **{ctx.author}**, you are missing the **Ban Members** permission.',
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)
        raise error

def setup(client):
    client.add_cog(ban(client))
