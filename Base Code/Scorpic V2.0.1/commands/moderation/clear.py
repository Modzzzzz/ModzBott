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
        await ctx.channel.purge(limit=amount+1)
        embed = discord.Embed(
            title='Channel Cleaning',
            description='Successfully cleared the channel!',
            color=discord.Color.green()
        )
        embedsent = await ctx.send(embed=embed)
        await asyncio.sleep(7.5)
        await embedsent.delete()
    

def setup(client):
    client.add_cog(clear(client))
