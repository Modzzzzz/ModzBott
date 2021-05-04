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

    # Kick command for users to request support by using s!kick @user {reason}
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        try:
            await member.kick(reason=reason)
            embed = discord.Embed(
                title='Member Kicked',
                description=f'**{member}** has been kicked from the server by **{ctx.author}** for **{reason}**',
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)
        # If the bot does not have the permission
        except discord.Forbidden:
            errorembed = discord.Embed(
                title='Bot Missing Permission',
                description=':x: I need the **Kick Members** permission to kick people!',
                color=discord.Color.red()
            )
            await ctx.send(embed=errorembed)

    # If the user does not have the permission
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                title='Missing Permissions',
                description=f':x: **{ctx.author}**, you are missing the **Kick Members** permission.',
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)
        raise error

def setup(client):
    client.add_cog(kick(client))
