import discord

from discfactbot import joke as jk
from discord.ext import commands


'''
this discord library revolves around the concept of event.
event is something you listen to and the respond to event.
for example : when a message happen in discord you will receive an
event about it than you resond to it.
discord.py is asynchronous library so things are done with callbacks
callback is function that is called when something else happen
'''
TOKEN='ODA4Njk1NTQyNTAxNzM2NDc5.YCKSag.ZfYS6EGmD2xHtvN3BwfM9ogjdQE'
client=commands.Bot(command_prefix="--",help_command=None)



@client.command(name='Setup')
async def Setup(message):
    guild=message.guild
    channelname="joke-and-fact"
    embed=discord.Embed(title='Success',description="joke & fact channel has been successfully created.",colour=0xff0000)
    await guild.create_text_channel(name=channelname)
    await message.send(embed=embed)

@client.event
async def on_memeber_join(member):
    for channel in member.server.channels:
        if str(channel)=='general':
            await client.send_message(f"""Welcome to the server {member}""")

@client.event# to register an event
async def on_ready():# this will call when bot is ready to use
    print('we have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    channels = ['joke-and-fact']
    type_of_joke=['PROGRAMMING','MISC','DARK','PUN','SPOOKY','CHRISTMAS']
    if message.author==client.user:
        return None

    if message.channel.name in channels:# bot only run command in joke-only channel
        if message.content.startswith('pls'):
            msg= message.content.split(' ')
            if len(msg)==2:
                joke=jk.get_joke()
                embed=discord.Embed(description=joke)
                await message.channel.send(embed=embed)

            elif len(msg)==3:
                if msg[2].upper() in type_of_joke:
                    joke = jk.get_joke(msg[2].upper())#get joke
                    embed = discord.Embed(description=joke,colour=0xff0000)
                    await message.channel.send(embed=embed)
                elif msg[2] == 'dadjoke':
                    joke = jk.get_dad_joke()
                    embed = discord.Embed(description=joke,colour=0xff0000)
                    await message.channel.send(embed=embed)
                else:
                    embed=discord.Embed(description="Wrong joke type")
                    await message.channel.send(embed=embed,colour=0xff0000)

            else:
                embed = discord.Embed(description="Invalid input")
                await message.channel.send("Invalid input")

    if message.content.upper()=='--SETUP':
        channels.append('joke-and-fact')
        await client.process_commands(message)
    # if message.content.upper()=='--SETUP':
    #     name='joke & fact'
    #     ch=discord.Guild(data=None,state=None)
    #     channels = await discord.Guild.create_text_channel(name=name)

    # print(f"""User : {message.author} tried to do command {message.cont} channel""")

client.run(TOKEN)