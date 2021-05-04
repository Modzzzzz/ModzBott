from discord.ext import commands
import discord

class slowmode(commands.Cog):
    def __init__(self, client):
        self.client = client

    # When the cog boots up on bot launch:
    # It will print 'Slowmode Cog registered.'

    @commands.Cog.listener()
    async def on_ready(self):
        print("Slowmode Cog registered.")

    # Slowmode command for users to request support by using s!slowmode {duration}
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def slowmode(self, ctx, seconds: int):
        try:
            await ctx.channel.edit(slowmode_delay=seconds)
            embed = discord.Embed(
                title='Channel Slowmode',
                description=f'The slowmode of this channel has been set to **{seconds}** seconds!',
                color=discord.Color.purple()
            )
            await ctx.send(embed=embed)
            # If the bot does not have the permission
        except discord.Forbidden:
            errorembed = discord.Embed(
                title='Bot Missing Permissions',
                description=':x: I need the **Manage Channels permission to set channel slow modes!',
                color=discord.Color.red()
            )
            await ctx.send(embed=errorembed)

    # If the user does not have the permission
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                title='Missing Permissions',
                description=f':x: **{ctx.author}**, you are missing the **Manage Channels** permission.',
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)
        raise error
    

def setup(client):
    client.add_cog(slowmode(client))
