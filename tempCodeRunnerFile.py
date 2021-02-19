import random
import discord
r = random.randint(0, 255)
g = random.randint(0, 255)
b = random.randint(0, 255)
color = discord.Colour.from_rgb(r,g,b)
print(type(color))