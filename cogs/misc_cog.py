from discord.ext.commands import Cog
from discord.ext.commands import CheckFailure
from discord.ext.commands import command, has_permissions
import discord

from Resources import config

client_obj = config.Database_oauth()
client = client_obj.database_info()
db = client['meme']
collection = db['server_info']


class Misc(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command(name="prefix")
    @has_permissions(manage_guild=True)
    async def change_prefix(self, ctx, new: str):
        if len(new) >= 3:
            embed = discord.Embed(title="Failed", description="The prefix can not be more than 5 characters in length",
                                  colour=0x00ff00)
            await ctx.channel.send(embed=embed)
        else:
            new_prefix = new + ' '
            collection.update_one({"server_id": ctx.guild.id}, {"$set": {"command_prefix": new_prefix}})
            embed = discord.Embed(title="Success", description=f"Prefix set to {new_prefix}.", colour=0xff0000)
            await ctx.channel.send(embed=embed)

    @change_prefix.error
    async def change_prefix_error(self, ctx, exc):
        if isinstance(exc, CheckFailure):
            embed = discord.Embed(title="Failed", description="You need the Manage Server permission to do that")
            await ctx.channel.send(embed=embed)

    @Cog.listener()
    async def on_ready(self):
        print("Misc cog is ready")


def setup(client):
    client.add_cog(Misc(client))
