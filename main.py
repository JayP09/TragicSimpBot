import discord
from discfactbot import joke as jk

'''
this discord library revolves around the concept of event.
event is something you listen to and the respond to event.
for example : when a message happen in discord you will receive an
event about it than you resond to it.
discord.py is asynchronous library so things are done with callbacks
callback is function that is called when something else happen
'''
TOKEN='ODA4Njk1NTQyNTAxNzM2NDc5.YCKSag.ZfYS6EGmD2xHtvN3BwfM9ogjdQE'
client=discord.Client()

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
    channels = ["joke-only"]
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
                    joke = jk.get_joke(msg[2].upper()) #get joke 
                    embed = discord.Embed(description=joke)
                    await message.channel.send(embed=embed)
                elif msg[2] == 'dadjoke':
                    joke = jk.get_dad_joke()
                    embed = discord.Embed(description=joke)
                    await message.channel.send(embed=embed)
                else:
                    embed=discord.Embed(description="Wrong joke type")
                    await message.channel.send(embed=embed)

            else:
                embed = discord.Embed(description="Invalid input")
                await message.channel.send("Invalid input")

    # print(f"""User : {message.author} tried to do command {message.cont} channel""")

client.run(TOKEN)