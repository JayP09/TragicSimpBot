import discord
from discord.ext import commands
import random


def colour_generator():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return discord.Colour.from_rgb(r, g, b)


class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Help Cog ready")

    @commands.command(name="help", aliases=['Help', 'HElp', 'HELp', 'HELP', 'hELP', 'heLP', 'helP', 'HeLp', 'hElP'])
    async def help(self, message, help_type="None"):
        channels = ['joke-and-fact']
        if message.channel.name in channels:
            if help_type.upper() == 'NONE':
                embed = discord.Embed(title="Bot Commands List", description="we have some really amazing commands",
                                      colour=colour_generator())
                embed.add_field(name='<:facts:814823810263547924> Facts', value="`pls help fact`", inline=True)
                embed.add_field(name='<:joke:814826126668726292> Joke', value="`pls help joke`", inline=True)
                embed.add_field(name='<:meme:814824521324036096> Meme', value="`pls help meme`", inline=True)
                embed.add_field(name='<:fire:814825327833382942> Motivation', value="`pls help motivation`",
                                inline=True)
                embed.add_field(name='<:setup:814828505275170856> Setup', value="`pls help setup`", inline=True)
                await message.channel.send(embed=embed)
            elif help_type.upper() == 'FACT':
                embed = discord.Embed(title="<:facts:814823810263547924> Fact Commands", colour=colour_generator())
                embed.add_field(name='<:facts:814823810263547924> Facts', value="`pls fact` return random fact")
                embed.add_field(name='<:random_number:814836293736595476> Random Number fact',
                                value="`pls fact number` return random number fact")
                embed.add_field(name='<:number:814844517508317246> Number fact', value='''`pls fact number` at place of number input any number. 
                                                                                         example:`pls fact 100`''')
                embed.add_field(name='<:date_fact:814836293582061618> Date fact', value='''`pls fact date` at place of date input any date in ""mm/dd"" format.
                                                                                        Example:`pls fact 06/09` ''')
                embed.add_field(name=' <:thinking_gorilla:814818580813578261> Animals',
                                value="`pls fact animal` return random animal fact")
                embed.add_field(name='<:doge:814824520916533249> Dog fact', value="`pls fact dog` return dog fact")
                embed.add_field(name='<:cat_fact:814818758421512203> Cat fact', value="`pls fact cat` return cat fact")
                embed.add_field(name='<:panda:814836293657034773> Panda fact',
                                value="`pls fact panda` return panda fact")
                embed.add_field(name='<:fox_fact:814836293409964033> Fox fact', value="`pls fact fox` return fox fact")
                embed.add_field(name='<:bird_fact:814836293343117323> Bird fact',
                                value="`pls fact bird` return bird fact")
                embed.add_field(name='<:koala_fact:814836293648646154> Koala fact',
                                value="`pls fact koala` return koala fact")
                await message.channel.send(embed=embed)
            elif help_type.upper() == 'MEME':
                embed = discord.Embed(title="<:meme:814824521324036096> Meme Commands", colour=colour_generator())
                embed.add_field(name="meme", value="`pls meme` return random meme from reddit")
                embed.add_field(name='Meme from specific page',
                                value="`pls meme pagename` at place of pagename input reddit page name for meme."
                                      " Example:`pls meme dark`")
                embed.add_field(name='meme command', value="`meme pagename` return hot,new meme from page.")
                embed.add_field(name="Meme Page List:",
                                value="`funny`, `dankmemes`, `memes`, `teenagers`, `Chodi`, `DsyncTV`, `cursedcomments`, `holdup`,`SaimanSays/`, `wholesomememes`, `IndianMeyMeys`, `indiameme`, `desimemes`, `Tinder`,`2meirl4meirl,`ComedyCemetery`, `terriblefacebookmemes`")
                await message.channel.send(embed=embed)
            elif help_type.upper() == 'JOKE':
                embed = discord.Embed(title=" <:joke:814826126668726292> Joke commands", colour=colour_generator())
                embed.add_field(name="<:meme:814824521324036096> Joke", value="`pls joke` return random joke ")
                embed.add_field(name="<:programming:814836293061312553> Programming Jokes",
                                value="`pls joke programming`")
                embed.add_field(name="<:misc:814836293095391243> Misc Jokes", value="`pls joke misc`")
                embed.add_field(name="<:dark:814837484461621258> Dark Jokes", value="`pls joke dark`")
                embed.add_field(name="<:pun:814836293301174343> Pun Jokes", value="`pls joke pun`")
                embed.add_field(name="<:spooky:814836293451513866> Spooky Jokes", value="`pls joke spooky`")
                embed.add_field(name="<:christmas:814836292974149643> Christmas Jokes", value="`pls joke christmas`")
                await message.channel.send(embed=embed)
            elif help_type.upper() == 'MOTIVATION':
                embed = discord.Embed(title="<:fire:814825327833382942> Motivation Commands", colour=colour_generator())
                embed.add_field(name="Motivational quote", value="`pls motivation`")
                embed.add_field(name="Motivational quote by category", value="`pls motivation category`")
                embed.add_field(name="Motivational quote of day",value="`pls motivation qotd`")
                embed.add_field(name="Motivational Category list:",value="`MOTIVATION`, `inspiration`, `inspire`, `motivational`, `productive`")
                await message.channel.send(embed=embed)
            else:
                embed =discord.Embed(title="Falied",colour=0x00ff00)
                embed.set_image(url="https://media.giphy.com/media/HNEmXQz7A0lDq/giphy.gif")
                await message.channel.send(embed=embed)


def setup(client):
    client.add_cog(Help(client))
