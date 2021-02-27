import discord
from discord.ext import commands
import random
from Resources import config


client_obj = config.Database_oauth()
client = client_obj.database_info()
db = client["meme"]
collection = db["server_info"]


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
        data = collection.find_one({'server_id': message.guild.id})
        prefix = data['command_prefix']
        if message.channel.name in channels:
            if help_type.upper() == 'NONE':
                embed = discord.Embed(title="Bot Commands List", description="we have some really amazing commands",
                                      colour=colour_generator())
                embed.add_field(name='<:facts:814823810263547924> Facts', value=f"`{prefix}help fact`", inline=True)
                embed.add_field(name='<:joke:814826126668726292> Joke', value=f"`{prefix}help joke`", inline=True)
                embed.add_field(name='<:meme:814824521324036096> Meme', value=f"`{prefix}help meme`", inline=True)
                embed.add_field(name='<:fire:814825327833382942> Quote', value=f"`{prefix}help quote`",
                                inline=True)
                embed.add_field(name='<:setup:814828505275170856> Setup', value=f"`{prefix}help setup`", inline=True)
                await message.channel.send(embed=embed)

            elif help_type.upper() == 'FACT':
                embed = discord.Embed(title="<:facts:814823810263547924> Fact Commands", colour=colour_generator())
                embed.add_field(name='<:facts:814823810263547924> Random Facts', value=f"`{prefix}fact` ")
                embed.add_field(name='<:random_number:814836293736595476> Random Number fact',
                                value=f"`{prefix}fact number` ")
                embed.add_field(name='<:number:814844517508317246> Number fact',
                                value=f"`{prefix}fact number`\n example:`{prefix}fact 100`")
                embed.add_field(name='<:date_fact:814836293582061618> Date fact',
                                value=f"`{prefix}fact date`\n at place of date input any date in ""mm/dd"" format.\n Example:`pls fact 06/09`",
                                inline=False)
                embed.add_field(name=' <:thinking_gorilla:814818580813578261> Animals',
                                value=f"`{prefix}fact animal` ")
                embed.add_field(name='<:doge:814824520916533249> Dog fact', value=f"`{prefix}fact dog` ")
                embed.add_field(name='<:cat_fact:814818758421512203> Cat fact', value=f"`{prefix}fact cat` ")
                embed.add_field(name='<:panda:814836293657034773> Panda fact',
                                value="`pls fact panda` ")
                embed.add_field(name='<:fox_fact:814836293409964033> Fox fact', value=f"`{prefix}fact fox` ")
                embed.add_field(name='<:bird_fact:814836293343117323> Bird fact',
                                value=f"`{prefix}fact bird` ")
                embed.add_field(name='<:koala_fact:814836293648646154> Koala fact',
                                value=f"`{prefix}fact koala` ")
                await message.channel.send(embed=embed)


            elif help_type.upper() == 'MEME':
                embed = discord.Embed(title="<:meme:814824521324036096> Meme Commands", colour=colour_generator())
                embed.add_field(name="<:dankmeme:814837484734382110>meme", value=f"`{prefix}meme`")
                embed.add_field(name='<:dankmeme:814837484734382110>meme command',
                                value="`meme pagename` \n return hot,new meme from any reddit page u desire.",
                                inline=False)
                embed.add_field(name='<:dankmeme:814837484734382110>Meme from specific page',
                                value=f"`{prefix}meme pagename` \n input pagename from memepage list given below "
                                      "\nExample:`pls meme dark`", inline=False)
                embed.add_field(name="Meme Page List:",
                                value="`funny`, `dankmemes`, `memes`, `teenagers`, `Chodi`, `DsyncTV`, `cursedcomments`, `holdup`,`SaimanSays/`, `wholesomememes`, `IndianMeyMeys`, `indiameme`, `desimemes`, `Tinder`,`2meirl4meirl`,`ComedyCemetery`, `terriblefacebookmemes`")

                await message.channel.send(embed=embed)


            elif help_type.upper() == 'JOKE':
                embed = discord.Embed(title=" <:joke:814826126668726292> Joke commands", colour=colour_generator())
                embed.add_field(name="<:meme:814824521324036096> Joke", value=f"`{prefix}joke` ")
                embed.add_field(name="<:programming:814836293061312553> Programming Jokes",
                                value=f"`{prefix}joke programming`")
                embed.add_field(name="<:misc:814836293095391243> Misc Jokes", value=f"`{prefix}joke misc`")
                embed.add_field(name="<:dark:814837484461621258> Dark Jokes", value=f"`{prefix}joke dark`")
                embed.add_field(name="<:pun:814836293301174343> Pun Jokes", value=f"`{prefix}joke pun`")
                embed.add_field(name="<:spooky:814836293451513866> Spooky Jokes", value=f"`{prefix}joke spooky`")
                embed.add_field(name="<:christmas:814836292974149643> Christmas Jokes",
                                value=f"`{prefix}joke christmas`")
                await message.channel.send(embed=embed)


            elif help_type.upper() == 'QUOTE':
                embed = discord.Embed(title="<:fire:814825327833382942> Quote Commands", colour=colour_generator())
                embed.add_field(name="Random quote", value=f"`{prefix} quote`")
                embed.add_field(name="Quote by category", value=f"`{prefix}quote category`")
                embed.add_field(name="Quote of day", value=f"`{prefix}quote qotd`")
                embed.add_field(name="Quotes Category list:",
                                value="`MOTIVATION`, `inspiration`, `inspire`, `motivational`, `productive`")
                await message.channel.send(embed=embed)
            elif help_type.upper() == 'SETUP':
                embed = discord.Embed(title="<:setup:814828505275170856>Setup Commands", colour=colour_generator())
                embed.add_field(name="First time Setup", value=f"`{prefix}setup`\n"
                                                               f"above command create joke-and-fact channel and certain roles in your server")
                embed.add_field(name="Change Prefix",value=f"`{prefix}prefix your_prefix`\n"
                                                           f"Example:"f"{prefix}"" is default prefix.if you want to change prefix to cls\n"
                                                           f"`{prefix}prefix cls` this command will change prfix to cls")
                embed.set_footer(text="Default prefix is pls")
                await message.channel.send(embed=embed)

            else:
                embed = discord.Embed(title="Falied", colour=0x00ff00)
                gif_list = ['http://gph.is/2cPVZfL','http://gph.is/1SuCOVi','http://gph.is/16sUz2u','http://gph.is/16sUz2u','http://gph.is/16sUz2u','http://gph.is/XKdD7x','https://gph.is/g/4bxR80v','https://media.giphy.com/media/HNEmXQz7A0lDq/giphy.gif','https://gph.is/g/4zWL7wK','https://gph.is/g/ZWpQOd4']
                embed.set_image(url = random.choice(gif_list))
                await message.channel.send(embed=embed)
def setup(client):
    client.add_cog(Help(client))
