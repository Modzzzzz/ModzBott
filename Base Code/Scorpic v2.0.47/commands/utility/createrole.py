from discord.ext import commands
import discord

class createrole(commands.Cog):
    def __init__(self, client):
        self.client = client

    # When the cog boots up on bot launch:
    # It will print 'Create Role Cog registered.'

    @commands.Cog.listener()
    async def on_ready(self):
        print("Create Role Cog registered.")

    # Create Role command for users to request support by using s!createrole {name}
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def createrole(self, ctx, *, name):
        try:
            await ctx.guild.create_role(name=name)
            embed = discord.Embed(
                title='Role Created',
                description=f':white_check_mark: I have created the role **{name}**',
                color=discord.Color.purple()
            )
            await ctx.send(embed=embed)
        # If the bot does not have the permission
        except discord.Forbidden:
            errorembed = discord.Embed(
                title='Bot Missing Permissions',
                description=':x: I need the **Manage Roles** permission to create roles!',
                color=discord.Color.red()
            )
            await ctx.send(embed=errorembed)

    # If the user does not have the permission
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                title='Missing Permissions',
                description=f':x: **{ctx.author}**, you are missing the **Manage Roles** permission.',
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)
        raise error


def setup(client):
    client.add_cog(createrole(client))
