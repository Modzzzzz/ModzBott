from discord.ext import commands
import discord
import asyncio

class clear(commands.Cog):
    def __init__(self, client):
        self.client = client

    # When the cog boots up on bot launch:
    # It will print 'Defaultcommands Cog registered.'

    @commands.Cog.listener()
    async def on_ready(self):
        print("Clear Cog registered.")

    # Help command for users to request support by using s!help
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=100):
        try:
            await ctx.channel.purge(limit=amount+1)
            embed = discord.Embed(
                title='Channel Cleaning',
                description='Successfully cleared the channel!',
                color=discord.Color.green()
            )
            embedsent = await ctx.send(embed=embed)
            await asyncio.sleep(7.5)
            await embedsent.delete()
        # If the bot does not have the permission
        except discord.Forbidden:
            errorembed = discord.Embed(
                title='Bot Missing Permissions',
                description=':x: I need the **Manage Messages** permission to clear messages!',
                color=discord.Color.red()
            )
            await ctx.send(embed=errorembed)
    
    # If the user does not have the permission
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                title='Missing Permissions',
                description=f':x: **{ctx.author}**, you are missing the **Manage Messages** permission.',
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)
        raise error

def setup(client):
    client.add_cog(clear(client))
