from discord.ext import commands
import discord

class createvc(commands.Cog):
    def __init__(self, client):
        self.client = client

    # When the cog boots up on bot launch:
    # It will print 'Create Voice Channel Cog registered.'

    @commands.Cog.listener()
    async def on_ready(self):
        print("Create Voice Channel Cog registered.")

    # Create Voice Channel command for users to request support by using s!createvc {name}
    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def createvc(self, ctx, *, name):
        try:
            await ctx.guild.create_voice_channel(name=name)
            embed = discord.Embed(
                title='Voice Channel Created',
                description=f':white_check_mark: I have created the voice channel **{name}**',
                color=discord.Color.purple()
            )
            await ctx.send(embed=embed)
        # If the bot does not have the permission
        except discord.Forbidden:
            errorembed = discord.Embed(
                title='Bot Missing Permissions',
                description=':x: I need the **Manage Channels** permission to create voice channels!',
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
    client.add_cog(createvc(client))
