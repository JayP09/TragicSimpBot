import discord
from discord.ext import commands
from Resources import motivation as mv
import random


def colour_generator():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return discord.Colour.from_rgb(r, g, b)


class Motivation(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Motivation Cog ready")

    @commands.command(name="quote", aliases=['Quote', 'QUOTE', 'QuotE'])
    async def fact(self, message, motivation_type="None"):
        channels = ['joke-and-fact']
        motivation_Category = ['MOTIVATION', 'inspiration', 'inspire', 'motivational', 'productive']
        if message.channel.name in channels:
            if motivation_type.upper() == 'NONE':
                quote, author = mv.quotes_fav()
                embed = discord.Embed(title='"'+quote+'"', description="-" + author, colour=colour_generator())
                await message.channel.send(embed=embed)
            elif motivation_type.upper() in motivation_Category:
                quote, author = mv.quotes_fav()
                embed = discord.Embed(title='"'+quote+'"', description="-" + author, colour=colour_generator())
                await message.channel.send(embed=embed)
            elif motivation_type.upper() == "QOTD":
                quote, author = mv.random_quote_fav()
                embed = discord.Embed(title='"'+quote+'"', description="-" + author, colour=colour_generator())
                await message.channel.send(embed=embed)
            else:
                pass
        else:
            # embed = discord.Embed(
            #     description=f"{message.author.mention} pls send command in joke-and-fact only channel",
            #     colour=colour_generator())
            embed = discord.Embed(title="Falied", colour=0x00ff00)
            gif_list = ['http://gph.is/2cPVZfL','http://gph.is/1SuCOVi','http://gph.is/16sUz2u','http://gph.is/16sUz2u','http://gph.is/16sUz2u','http://gph.is/XKdD7x','https://gph.is/g/4bxR80v','https://media.giphy.com/media/HNEmXQz7A0lDq/giphy.gif','https://gph.is/g/4zWL7wK','https://gph.is/g/ZWpQOd4']
            embed.set_image(url = random.choice(gif_list))
            await message.channel.send(embed=embed)


def setup(client):
    client.add_cog(Motivation(client))
