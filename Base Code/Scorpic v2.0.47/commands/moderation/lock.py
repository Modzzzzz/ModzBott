from discord.ext import commands
import discord

class lock(commands.Cog):
    def __init__(self, client):
        self.client = client

    # When the cog boots up on bot launch:
    # It will print 'Lock Cog registered.'

    @commands.Cog.listener()
    async def on_ready(self):
        print("Lock Cog registered.")

    # Lock command for users to lock channels by using s!lock in the channel
    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def lock(self, ctx, channel : discord.TextChannel=None):
        try:
            channel = ctx.channel
            overwrite = channel.overwrites_for(ctx.guild.default_role)
            overwrite.send_messages = False
            embed = discord.Embed(
                title='Channel Locked',
                description=f':lock: This channel has been locked by **{ctx.author}**. Please come back soon.',
                color=discord.Color.purple()
            )
            await ctx.send(embed=embed)
            await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
        # If the bot does not have the permission
        except discord.Forbidden:
            errorembed = discord.Embed(
                title='Bot Missing Permissions',
                description=':x: I need the **Manage Channels** permission to lock channels!',
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
    client.add_cog(lock(client))
