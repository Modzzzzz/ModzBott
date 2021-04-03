from discord.ext import commands
import discord

class whois(commands.Cog):
    def __init__(self, client):
        self.client = client

    # When the cog boots up on bot launch:
    # It will print 'Who Is Cog registered.'

    @commands.Cog.listener()
    async def on_ready(self):
        print("Who Is Cog registered.")

    # Who Is command for users to server info by using s!whois @user
    @commands.command()
    async def whois(self, ctx, *, member: discord.Member = None):
        embed = discord.Embed(
            color=discord.Color.green()
        )
        embed.add_field(name='Member Name:', value=f"```{member}```", inline=True)
        embed.add_field(name='Member ID:', value=f'```{member.mention}```', inline=True)
        embed.set_thumbnail(url=f"{member.avatar_url}")
        await ctx.channel.send(embed=embed)

def setup(client):
    client.add_cog(whois(client))
