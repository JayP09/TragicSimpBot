import discord
from discord.ext import commands
from Resources import server as sr
from Resources import meme_creator_db as me
import random
from cogs import levelsys, fact_cog, joke_cog, meme_cog, motivation_cog, help_cog

'''
this discord library revolves around the concept of event.
event is something you listen to and the respond to event.
for example : when a message happen in discord you will receive an
event about it than you respond to it.
discord.py is asynchronous library so things are done with callbacks
callback is function that is called when something else happen
'''
TOKEN = 'ODA4Njk1NTQyNTAxNzM2NDc5.YCKSag.ZfYS6EGmD2xHtvN3BwfM9ogjdQE'
cogs = [levelsys, fact_cog, joke_cog, meme_cog, motivation_cog, help_cog]
OWNER_IDS = [252353540327079936, 669518518777282561]
roles_meme = ['NoobMemer', 'MemeRular', 'MemeStar', 'AlphaMemer']
client = commands.Bot(command_prefix=("pls ", "PLS", 'Pls ', 'pLs ', 'plS '), aliases=['PLS ', 'Pls ', 'pLs ', 'plS '],
                      owner_ids=OWNER_IDS, help_command=None)


def full_run():
    for i in range(len(cogs)):
        cogs[i].setup(client)

    @client.command(name='setup')
    @commands.has_permissions(manage_roles=True)
    async def setup(message):  # when member type --setup command
        guild = message.guild
        channel_name = "joke-and-fact"
        text_channel_list, roles_list = sr.get_server_info(guild.name)
        if channel_name in text_channel_list:
            embed = discord.Embed(
                title='Failed',
                description="joke & fact channel already exist",
                colour=0xff0000)
            await message.send(embed=embed)
        else:
            await guild.create_text_channel(name=channel_name)  # create text channel in server
            sr.update_channel_info(channel_name, guild.name)
            embed = discord.Embed(
                title='Success',
                description="joke & fact channel has been successfully created.",
                colour=0xff0000)
            await message.send(embed=embed)

        # to create role for meme
        for role in roles_meme:
            if role in roles_list:
                continue
            else:
                await guild.create_role(name=role, colour=discord.Colour.random())
                sr.update_server_roles_info(roles_meme, guild.name)

    @client.event
    async def on_guild_channel_delete(channel):
        channel_name = channel.name
        guild = channel.guild
        sr.update_server_info(guild.name, channel_name)

    @client.event
    async def on_guild_channel_create(channel):
        channel_name = channel.name
        guild = channel.guild
        sr.update_server_info(guild.name, channel_name)

    @client.event
    async def on_connect():
        print(" bot connected")

    @client.event
    async def on_disconnect():
        print("bot disconnected")

    @client.event
    async def on_member_join(member):  # when member join the server
        for channel in member.server.channels:
            if str(channel) == 'general':
                await member.server.channel.send(f"""Welcome to the server {member}""")

    @client.event
    async def on_member_join(self, member):
        pass

    @client.event  # to register an event
    async def on_ready():  # this will call when bot is ready to use
        print('we have logged in as {0.user}'.format(client))
        for guild in client.guilds:
            server_name = guild.name
            channel_guild = guild.text_channels
            role_guild = guild.roles
            text_channels_list = []
            roles_list = []
            for role in role_guild:
                roles_list.append(role.name)
            for channel in channel_guild:
                text_channels_list.append(channel.name)
            sr.add_server_info(server_name, text_channels_list, roles_list)

    def colour_generator():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return discord.Colour.from_rgb(r, g, b)

    @client.event
    async def on_message(message):
        channels = ['joke-and-fact']
        if message.author == client.user:
            return None

        if message.channel.name in channels:
            if message.content.startswith('meme'):
                msg = message.content.split(' ')
                try:
                    page, title, url = me.single_meme(msg[1])
                    if page is None:
                        embed = discord.Embed(title=title, colour=colour_generator())
                        embed.set_image(url=url)
                        await message.channel.send(embed=embed)
                    else:
                        embed = discord.Embed(title=title, url=url, colour=colour_generator())
                        embed.set_image(url=url)
                        embed.set_footer(text="r/" + page)
                        await message.channel.send(embed=embed)
                except:
                    print("Not meme page name")

        await client.process_commands(message)  # code to execute commands

    client.run(TOKEN)


if __name__ == "__main__":
    full_run()
