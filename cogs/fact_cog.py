import discord
from discord.ext import commands
from discfactbot.Resources import fact as ft
import re

bot_channel = 'joke-and-fact'


class Fact(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("fact cog is ready")

    @commands.command(name="fact", aliases=['Fact', 'FACT', 'FAct', 'FaCt', 'FACt', 'facT'])
    async def fact(self, message, fact_type="None"):
        channels = ['joke-and-fact']
        if message.channel.name in channels:  # bot only run command in joke-only channel
            if fact_type == "None":
                fact = ft.get_fact()  # return random fact
                embed = discord.Embed(description=fact, colour=0x00ff00)
                await message.channel.send(embed=embed)
            elif fact_type.upper() == 'NUMBER':
                n_fact = ft.get_random_number_fact()  # return random number fact
                embed = discord.Embed(description=n_fact, colour=0x00ff00)
                await message.channel.send(embed=embed)
            elif fact_type.isdigit():
                n_fact = ft.get_number_fact(fact_type)  # return number fact
                embed = discord.Embed(description=n_fact, colour=0x00ff00)
                await message.channel.send(embed=embed)
            elif re.match(r'\d{2}/\d{2}', fact_type):
                n_fact = ft.get_date_fact(fact_type)  # return date fact
                embed = discord.Embed(description=n_fact, colour=0x00ff00)
                await message.channel.send(embed=embed)
            elif fact_type.upper() == 'ANIMAL':  # return random animals fact
                animals_fact = ft.get_animals_fact()
                embed = discord.Embed(description=animals_fact, colour=0x00ff00)
                await message.channel.send(embed=embed)
            elif fact_type.upper() == 'DOG':  # return dog fact
                animals_fact = ft.animal_fact(fact_type)
                embed = discord.Embed(description=animals_fact, colour=0x00ff00)
                await message.channel.send(embed=embed)
            elif fact_type.upper() == 'CAT':  # return cat fact
                animals_fact = ft.animal_fact(fact_type)
                embed = discord.Embed(description=animals_fact, colour=0x00ff00)
                await message.channel.send(embed=embed)
            elif fact_type.upper() == 'PANDA':  # return panda fact
                animals_fact = ft.animal_fact(fact_type)
                embed = discord.Embed(description=animals_fact, colour=0x00ff00)
                await message.channel.send(embed=embed)
            elif fact_type.upper() == 'FOX':  # return fox fact
                animals_fact = ft.animal_fact(fact_type)
                embed = discord.Embed(description=animals_fact, colour=0x00ff00)
                await message.channel.send(embed=embed)
            elif fact_type.upper() == 'BIRD':  # return bird fact
                animals_fact = ft.animal_fact(fact_type)
                embed = discord.Embed(description=animals_fact, colour=0x00ff00)
                await message.channel.send(embed=embed)
            elif fact_type.upper() == 'KOALA':  # return koala fact
                animals_fact = ft.animal_fact(fact_type)
                embed = discord.Embed(description=animals_fact, colour=0x00ff00)
                await message.channel.send(embed=embed)
            else:
                embed = discord.Embed(
                    title='Invalid Input',
                    description='Please try command "pls fact" for random fact or type "pls fact number" '
                                'for random number fact',
                    colour=0xff0000)
                await message.channel.send(embed=embed)


def setup(client):
    client.add_cog(Fact(client))
