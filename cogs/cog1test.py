import discord
from discord.ext import commands

class Cogs(commands.Cog):
    def __init(self, client):
        self.client = client

    @commands.command()
    async def cogs_test(self, ctx):
        await ctx.send("cogs works yay")

    @commands.command(aliases = ["cogst"])
    async def cogs_test_2(self, ctx):
        await ctx.send("ok so this cog actually works")

def setup(client):
    client.add_cog(Cogs(client))
