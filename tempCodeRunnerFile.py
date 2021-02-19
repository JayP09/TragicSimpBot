import discord
import fact as ft
import joke as jk
from discord.ext import commands
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
async def setup(message):
    guild = message.guild
    channel_name = "joke-and-fact"
    embed = discord.Embed(
        title='Success',
        description="joke & fact channel has been successfully created.",
        colour=0xff0000)
    await guild.create_text_channel(name=channel_name)
    await message.send(embed=embed)


@client.event
async def on_member_join(member):
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
        if message.content.startswith('pls'):
            msg = message.content.split(' ')
            # code to execute joke
            if msg[1].upper() == 'JOKE':
                if len(msg) == 2:
                    joke = jk.get_joke()
                    embed = discord.Embed(description=joke, colour=0x0000ff)
                    await message.channel.send(embed=embed)
                elif len(msg) == 3:
                    if msg[2].upper() in type_of_joke:
                        joke = jk.get_joke(msg[2].upper())  # get joke
                        embed = discord.Embed(description=joke, colour=0x0000ff)
                        await message.channel.send(embed=embed)
                    elif msg[2] == 'dadjoke':
                        joke = jk.get_dad_joke()
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
                    fact = ft.get_fact()
                    embed = discord.Embed(description=fact, colour=0x00ff00)
                    await message.channel.send(embed=embed)
                elif msg[2].upper() == 'NUMBER':
                    n_fact = ft.get_random_number_fact()
                    embed = discord.Embed(description=n_fact, colour=0x00ff00)
                    await message.channel.send(embed=embed)
                elif msg[2].isdigit():
                    n_fact = ft.get_number_fact(msg[2])
                    embed = discord.Embed(description=n_fact, colour=0x00ff00)
                    await message.channel.send(embed=embed)
                elif re.match(r'\d{2}/\d{2}', msg[2]):
                    n_fact = ft.get_date_fact(msg[2])
                    embed = discord.Embed(description=n_fact, colour=0x00ff00)
                    await message.channel.send(embed=embed)
                else:
                    embed = discord.Embed(
                        title='Invalid Input',
                        description='Please try command "pls fact" for random fact or type "pls fact number" '
                                    'for random number fact',
                        colour=0xff0000)
                    await message.channel.send(embed=embed)

    await client.process_commands(message)


client.run(TOKEN)
