import discord
from discord.ext import commands
from Resources import meme_db as me
import random


def colour_generator():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return discord.Colour.from_rgb(r, g, b)


class Meme(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("meme Cog ready")

    @commands.command(name="meme", aliases=['Meme', 'MEme', 'MEMe', 'MEME', 'mEME', 'meME', 'memE', 'MeMe', 'mEmE'])
    async def fact(self, message, meme_type="None"):
        channels = ['joke-and-fact']
        page_list = ['funny', 'dankmemes', 'memes', 'teenagers', 'Chodi', "DsyncTV", 'cursedcomments', 'holdup',
                     'SaimanSays/', 'wholesomememes', 'IndianMeyMeys', 'indiameme', 'desimemes', 'Tinder',
                     '2meirl4meirl',
                     'ComedyCemetery', 'terriblefacebookmemes']
        if message.channel.name in channels:  # bot only run command in joke-only channel
            if meme_type.upper() == 'NONE':
                try:
                    meme_page, title, url = me.send_meme()
                except:
                    meme_page, title, url = me.send_meme()
                embed = discord.Embed(title=title, url=url,
                                      colour=colour_generator())  # discord.colour return hex colour
                embed.set_image(url=url)
                embed.set_footer(text="r/" + meme_page)
                await message.channel.send(embed=embed)
            elif meme_type in page_list:
                meme_page, title, url = me.send_specific_meme(meme_type)
                embed = discord.Embed(title=title, url=url, colour=colour_generator())
                embed.set_image(url=url)
                embed.set_footer(text="r/" + meme_page)
                await message.channel.send(embed=embed)
            else:
                embed = discord.Embed(title="Falied", colour=0x00ff00)
                gif_list =['https://media.giphy.com/media/TqiwHbFBaZ4ti/giphy.gif',
                            'https://media.giphy.com/media/3osxY9kuM2NGUfvThe/giphy.gif',
                            'https://media.giphy.com/media/YyKPbc5OOTSQE/giphy.gif',
                            'https://media.giphy.com/media/li0dswKqIZNpm/giphy.gif',
                            'https://media0.giphy.com/media/ljtfkyTD3PIUZaKWRi/giphy.gif',
                            'https://media.giphy.com/media/HNEmXQz7A0lDq/giphy.gif',
                            'https://media.giphy.com/media/4au7PZFkWSjnIsnZXL/giphy.gif',
                            'https://media1.giphy.com/media/3Z1oSJQpkDZBvJVsUT/giphy.gif',
                            'https://media.giphy.com/media/vKz8r5aTUFFJu/giphy.gif',
                            'https://media.giphy.com/media/kEtm4mSTbxvH7j3uCu/giphy.gif',
                            'https://media.giphy.com/media/bi6RQ5x3tqoSI/giphy.gif']
                embed.set_image(url = random.choice(gif_list))
                await message.channel.send(embed=embed)


def setup(client):
    client.add_cog(Meme(client))
