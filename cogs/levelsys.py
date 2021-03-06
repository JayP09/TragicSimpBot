import discord
from discord.ext import commands
import random
from Resources import config

bot_channel = 'joke-and-fact'
level = ['NoobMemer', 'MemeRular', 'MemeStar', 'AlphaMemer']
levelnum = [5, 10, 15, 20]
client_obj = config.Database_oauth()
client = client_obj.database_info()
# to connect mongodb server
db = client["meme"]
levelling = db["levelling"]


def user_level_info(current_xp, lvl):
    if current_xp > lvl * 100:
        current_xp = current_xp - lvl * 100
        lvl += 1
        return current_xp, lvl
    else:
        return current_xp, lvl


def update_user_roles_info(user_id, role):
    roles_list = levelling['user_roles']
    if role not in roles_list:
        roles_list.append(role)
    levelling.update_one({"user_id": user_id}, {"$set": {'user_roles': roles_list}})


def colour_generator():  # return random generated colour
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
        print("levelsys cog is ready")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content.lower() == '--rank':
            return None
        if message.channel.name in bot_channel:
            msg = message.content.split(' ')
            if msg[0].upper() == 'PLS' or msg[0].upper() == 'MEME':
                stats = levelling.find_one({"user_id": message.author.id})
                if not message.author.bot:
                    if stats is None:
                        role_guild = message.author.guild.roles
                        roles_list = []
                        for role in role_guild:
                            roles_list.append(role.name)
                        newuser = {"user_id": message.author.id, "username": message.author.name,
                                "server_name": message.guild.name,
                                "user_roles": roles_list,
                                "xp": 0,
                                "current_xp": 0,
                                "level": 1}
                        levelling.insert_one(newuser)  # insert user in database
                    else:
                        current_xp = stats['current_xp']
                        lvl = stats["level"]
                        xp = stats["xp"] + 10
                        current_xp += 10
                        cur_xp, user_level = user_level_info(current_xp, lvl)
                        levelling.update_one({"user_id": message.author.id},
                                             {"$set": {"current_xp": cur_xp, "xp": xp,
                                                       "level": user_level}})  # update Resources in mongodb database
                        if lvl >= user_level:
                            pass
                        else:
                            levelling.update_one({"user_id": message.author.id}, {"$set": {"level": user_level}})
                            embed = discord.Embed(
                                description=f"well done {message.author.mention}! You leveled up to **level: {user_level}**!",
                                colour=colour_generator())
                            await message.channel.send(embed=embed)
                            for i in range(len(level)):
                                if user_level == levelnum[i]:
                                    await message.author.add_roles(
                                        discord.utils.get(message.author.guild.roles, name=level[i]))
                                    update_user_roles_info(message.author.id, level[i])
                                    embed = discord.Embed(
                                        description=f"{message.author.mention} you have gotten role **{level[i]}**!!!")
                                    embed.set_thumbnail(url=message.author.avatar_url)  # assign role to user
                                    await message.channel.send(embed=embed)

    @commands.command()
    async def rank(self, ctx):  # give rank of user
        if ctx.channel.name == bot_channel:
            stats = levelling.find_one({"user_id": ctx.author.id})
            if stats is None:
                embed = discord.Embed(description="You haven't sent any messages, no rank!!!",
                                      colour=colour_generator())
                await ctx.channel.send(embed=embed)
            else:
                total_xp = stats['xp']
                current_xp = stats["current_xp"]
                lvl = stats['level']
                max_val = (lvl + 1) * 100
                box_ratio = int(max_val / 20)
                green_box = int(current_xp / box_ratio)
                white_box = 20 - green_box

                rank = 0
                rankings = levelling.find().sort("xp", -1)  # to sort the database

                for x in rankings:
                    rank += 1
                    if stats["user_id"] == x["user_id"]:
                        break
                embed = discord.Embed(title="{}'s level stats".format(ctx.author.name), description=ctx.author.mention,
                                      colour=colour_generator())
                embed.add_field(name="Total_xp", value=f'{total_xp}', inline=True)
                embed.add_field(name="XP", value=f"{current_xp}/{int(100 * (lvl + 1))}", inline=True)
                embed.add_field(name="Rank", value=f"{rank}/{ctx.guild.member_count}", inline=True)
                embed.add_field(name="Progress Bar [lvl]",
                                value=green_box * ":blue_square:" + (white_box) * ":white_large_square:", inline=True)
                embed.set_thumbnail(url=ctx.author.avatar_url)  # used to get user avatar
                await ctx.channel.send(embed=embed)

    @commands.command()
    async def leaderboard(self, ctx):  # generate leaderboard
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
