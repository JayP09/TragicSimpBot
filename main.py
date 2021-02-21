import discord
import fact as ft
import joke as jk
import meme_db as me
import random
from discord.ext import commands
import time
import re

'''
this discord library revolves around the concept of event.
event is something you listen to and the respond to event.
for example : when a message happen in discord you will receive an
event about it than you respond to it.
discord.py is asynchronous library so things are done with callbacks
callback is function that is called when something else happen
'''
TOKEN = 'ODA4Njk1NTQyNTAxNzM2NDc5.YCKSag.ZfYS6EGmD2xHtvN3BwfM9ogjdQE'
client = commands.Bot(command_prefix="--", help_command=None)


@client.command(name='setup')
async def setup(message):  # when member type --setup command
    guild = message.guild
    channel_name = "joke-and-fact"
    embed = discord.Embed(
        title='Success',
        description="joke & fact channel has been successfully created.",
        colour=0xff0000)
    await guild.create_text_channel(name=channel_name)  # create text channel in server
    await message.send(embed=embed)


@client.event
async def on_member_join(member):  # when member join the server
    for channel in member.server.channels:
        if str(channel) == 'general':
            await client.send_message(f"""Welcome to the server {member}""")


@client.event  # to register an event
async def on_ready():  # this will call when bot is ready to use
    print('we have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    channels = ['joke-and-fact']
    type_of_joke = ['PROGRAMMING', 'MISC', 'DARK', 'PUN', 'SPOOKY', 'CHRISTMAS']
    if message.author == client.user:
        return None

    if message.channel.name in channels:  # bot only run command in joke-only channel
        if message.content.startswith('pls'):  # bot only run when message is start with pls
            msg = message.content.split(' ')
            # code to execute joke
            if msg[1].upper() == 'JOKE':
                if len(msg) == 2:
                    joke = jk.get_joke()
                    embed = discord.Embed(description=joke,colour=0x0000ff)  # this is used to send embed text to discord
                    await message.channel.send(embed=embed)
                elif len(msg) == 3:
                    if msg[2].upper() in type_of_joke:
                        joke = jk.get_joke(msg[2].upper())  # return random joke
                        embed = discord.Embed(description=joke, colour=0x0000ff)
                        await message.channel.send(embed=embed)
                    elif msg[2] == 'dadjoke':
                        joke = jk.get_dad_joke()  # return dad joke
                        embed = discord.Embed(description=joke, colour=0x0000ff)
                        await message.channel.send(embed=embed)
                    else:
                        embed = discord.Embed(description="Wrong joke type", colour=0x0000ff)
                        await message.channel.send(embed=embed)
                else:
                    embed = discord.Embed(description="Invalid input", colour=0xff0000)
                    await message.channel.send(embed=embed)

            # code to execute fact
            if msg[1].upper() == 'FACT':
                if len(msg) == 2:
                    fact = ft.get_fact()  # return random fact
                    embed = discord.Embed(description=fact, colour=0x00ff00)
                    await message.channel.send(embed=embed)
                elif msg[2].upper() == 'NUMBER':
                    n_fact = ft.get_random_number_fact()  # return random number fact
                    embed = discord.Embed(description=n_fact, colour=0x00ff00)
                    await message.channel.send(embed=embed)
                elif msg[2].isdigit():
                    n_fact = ft.get_number_fact(msg[2])  # return number fact
                    embed = discord.Embed(description=n_fact, colour=0x00ff00)
                    await message.channel.send(embed=embed)
                elif re.match(r'\d{2}/\d{2}', msg[2]):
                    n_fact = ft.get_date_fact(msg[2])  # return date fact
                    embed = discord.Embed(description=n_fact, colour=0x00ff00)
                    await message.channel.send(embed=embed)
                else:
                    embed = discord.Embed(
                        title='Invalid Input',
                        description='Please try command "pls fact" for random fact or type "pls fact number" '
                                    'for random number fact',
                        colour=0xff0000)
                    await message.channel.send(embed=embed)

            # code to execute meme
            if msg[1].upper() == 'MEME':
                if len(msg) == 2:
                    # try:
                    meme_page, title, url = me.send_meme()
                    r = random.randint(0, 255)
                    g = random.randint(0, 255)
                    b = random.randint(0, 255)
                    embed = discord.Embed(title=title, url=url, colour=discord.Colour.from_rgb(r, g,b))  # discord.colour return hex colour
                    embed.set_image(url=url)
                    text = "r/" + meme_page
                    embed.set_footer(text=text)
                    await message.channel.send(embed=embed)
                    # except:
                    #     embed = discord.Embed(description='Sleeping for 1 min')
                    #     await message.channel.send(embed=embed)

                    # if rows == 1:
                    #     embed = discord.Embed(description='Sleeping for 1 min')
                    #     await message.channel.send(embed=embed)
                    #     time.sleep(60)
                elif len(msg) == 3:
                    pass
                else:
                    print("No meme to send. Try after 1 min")

    await client.process_commands(message)  # code to execute commands


client.run(TOKEN)
