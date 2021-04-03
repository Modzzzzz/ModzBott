from discord.ext import commands
import discord

class createchannel(commands.Cog):
    def __init__(self, client):
        self.client = client

    # When the cog boots up on bot launch:
    # It will print 'Create Text Channel Cog registered.'

    @commands.Cog.listener()
    async def on_ready(self):
        print("Create Text Channel Cog registered.")

    # Create Text Channel command for users to request support by using s!createchannel {name}
    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def createchannel(self, ctx, *, name):
        try:
            await ctx.guild.create_text_channel(name=name)
            embed = discord.Embed(
                title='Text Channel Created',
                description=f':white_check_mark: I have created the channel **{name}**',
                color=discord.Color.purple()
            )
            await ctx.send(embed=embed)
        # If the bot does not have the permission
        except discord.Forbidden:
            errorembed = discord.Embed(
                title='Bot Missing Permissions',
                description=':x: I need the **Manage Channels** permission to create text channels!',
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
    client.add_cog(createchannel(client))
