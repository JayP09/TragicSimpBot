from threading import current_thread
import discord
from discord.ext import commands
from pymongo import MongoClient
import random

bot_channel = 'joke-and-fact'
level = ['NoobMemer', 'MemeRular', 'MemeStar', 'AlphaMemer']
levelnum = [5, 10, 15, 20]

client = MongoClient(
    "mongodb+srv://BeLazy:BeLazy@cluster0.csr3d.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client["meme"]
levelling = db["levelling"]


def user_level_info(current_xp,xp,level):
    if current_xp > level*100:
        current_xp = current_xp-level*100
        level+=1
        return current_xp,level
    else:
        return current_xp,level

def colour_generator():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return discord.Colour.from_rgb(r, g, b)


class LevelSys(commands.Cog):
    def __init__(self, client):
        """

        :type client: client object from discord 
        """
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("ready")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content.lower() == '--rank':
            return None
        if message.channel.name in bot_channel:
            stats = levelling.find_one({"user_id": message.author.id})
            if not message.author.bot:
                if stats is None:
                    newuser = {"user_id": message.author.id, "username": message.author.name, "xp":0,"current_xp": 0, "level": 1}
                    levelling.insert_one(newuser)
                else:
                    current_xp = stats['current_xp']
                    level = stats["level"]
                    xp = stats["xp"] + 10
                    current_xp += 10
                    if current_xp > level*100:
                        current_xp = current_xp-level*100
                        level+=1
                        levelling.update_one({"user_id": message.author.id}, {"$set": {"current_xp":current_xp, "level": level}})
                    current_xp,user_level = user_level_info(current_xp,xp,level)
                    levelling.update_one({"user_id": message.author.id}, {"$set": {"current_xp":current_xp ,"xp": xp, "level": user_level}})
                    print(user_level)
                    if stats['level'] >= user_level:
                        print(user_level, "level not updated")
                    else:
                        print(user_level, "inside else")
                        levelling.update_one({"user_id": message.author.id}, {"$set": {"level": user_level}})
                        embed = discord.Embed(
                            description=f"well done {message.author.mention}! You leveled up to **level: {user_level}**!",
                            colour=colour_generator())
                        await message.channel.send(embed=embed)
                        for i in range(len(level)):
                            if user_level == levelnum[i]:
                                await message.author.add_roles(
                                    discord.utils.get(message.author.guild.roles, name=level[i]))
                                embed = discord.Embed(
                                    description=f"{message.author.mention} you have gotten role **{level[i]}**!!!")
                                embed.set_thumbnail(url=message.authr.avatar_url)
                                await message.channel.send(embed=embed)

    @commands.command()
    async def rank(self, ctx):
        if ctx.channel.name == bot_channel:
            stats = levelling.find_one({"user_id": ctx.author.id})
            if stats is None:
                embed = discord.Embed(description="You haven't sent any messages, no rank!!!",colour=colour_generator())
                await ctx.channel.send(embed=embed)
            else:
                xp = stats["xp"]
                lvl = user_level_info(xp)
                rank = 0
                boxes = int((xp / (100 * (lvl + 1)) * 10))
                rankings = levelling.find().sort("xp", -1)
                for x in rankings:
                    rank += 1
                    if stats["user_id"] == x["user_id"]:
                        break
                embed = discord.Embed(title="{}'s level stats".format(ctx.author.name), colour=colour_generator())
                embed.add_field(name="Name", value=ctx.author.mention, inline=True)
                embed.add_field(name="XP", value=f"{xp}/{int(100 * (lvl + 1))}", inline=True)
                embed.add_field(name="Rank", value=f"{rank}/{ctx.guild.member_count}", inline=True)
                embed.add_field(name="Progress Bar [lvl]",
                                value=boxes * ":blue_square:" + (20 - boxes) * ":white_large_square:", inline=True)
                embed.set_thumbnail(url=ctx.author.avatar_url)
                await ctx.channel.send(embed=embed)

    @commands.command()
    async def leaderboard(self, ctx):
        if ctx.channel.name == bot_channel:
            rankings = levelling.find().sort("xp", -1)
            i = 1
            embed = discord.Embed(title="Rankings:", colour=colour_generator())
            for x in rankings:
                try:
                    temp = ctx.guild.get_member(x["id"])
                    tempxp = x["xp"]
                    embed.add_field(name=f"{i}:{temp.name}", value=f"Total XP:{tempxp}", inline=False)
                    i += 1
                except:
                    pass
                if i == 11:
                    break
                await ctx.channel.send(embed=embed)


def setup(client):
    client.add_cog(LevelSys(client))