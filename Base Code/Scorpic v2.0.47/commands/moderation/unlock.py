from discord.ext import commands
import discord

class unlock(commands.Cog):
    def __init__(self, client):
        self.client = client

    # When the cog boots up on bot launch:
    # It will print 'Unlock Cog registered.'

    @commands.Cog.listener()
    async def on_ready(self):
        print("Unlock Cog registered.")

    # Unlock command for users to unlock channels by using s!unlock in the channel
    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def unlock(self, ctx, channel : discord.TextChannel=None):
        try:
            channel = ctx.channel
            overwrite = channel.overwrites_for(ctx.guild.default_role)
            overwrite.send_messages = True
            embed = discord.Embed(
                title='Channel Unlocked',
                description=f':white_check_mark: This channel has been unlocked by **{ctx.author}**!',
                color=discord.Color.green()
            )
            await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
            await ctx.send(embed=embed)
        # If the bot does not have the permission
        except discord.Forbidden:
            errorembed = discord.Embed(
                title='Bot Missing Permissions',
                description=':x: I need the **Manage Channels** permission to unlock channels!',
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
    client.add_cog(unlock(client))
