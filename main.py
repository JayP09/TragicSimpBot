import discord

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

@client.event# to register an event
async def on_ready():# this will call when bot is ready to use
    print('we have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author==client.user:
        return

    if message.content.startswith('pls'):
        await message.channel.send('Hello!')


client.run(TOKEN)