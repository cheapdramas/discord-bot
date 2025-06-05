from discord.ext import commands
from get_random_stuff import random_gif
from random import randint
from jsonchik import add_warn
import env

MAX_WARNINGS : int = env.getenv("MAX_WARNINGS")
APP_ID : int = env.getenv("APP_ID")


class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("Commands cog initialized")

    @commands.command()
    async def hello(self, ctx):
        print("greetings")
        await ctx.send(f"Hello {ctx.author.mention}!")

    
    @commands.command()
    async def gif(self, ctx):
        await ctx.send(random_gif())

    @commands.command()
    async def random_act(self, ctx):
        activities = ["Пузата в 16", "Коунтр Страйк", "порно", "osu motherfucker!"]
        activity = activities[randint(0, len(activities) - 1)]
        await ctx.send(activity)


    @commands.command()
    async def warn(self, ctx):
        channel = ctx.channel
        replied_message = await channel.fetch_message(ctx.message.reference.message_id)

        guild = ctx.guild
        replied_message_author = guild.get_member(replied_message.author.id)
        who_replied = guild.get_member(ctx.author.id)

        if replied_message.author.id == env.getenv("APP_ID"):
            await replied_message.add_reaction("😄")
            await ctx.send(
                f"{ctx.author.mention} ти ахуєл ето же я!!"
            )
            return


        await replied_message.add_reaction("💀")
        warn_count = add_warn(replied_message.author.id)
        await ctx.send(f"У {ctx.author.mention} ДО БАНА НАХУЙ ЗАЛИШИЛОСЬ: {MAX_WARNINGS - warn_count }")
        if warn_count == MAX_WARNINGS and not replied_message_author.guild_permissions.administrator and who_replied.guild_permissions.administrator:
            try:
                await ctx.send(f"{replied_message.author.mention} ПІЗДА НАСТАЛА ПОРОСЯ")
                await replied_message_author.ban(reason="нє уступіл мєсто в автобусе")
            except Exception as e:
                await ctx.send(f"❌ Помилка при бані: {e}")


        



async def setup(bot):
    if bot.get_cog("Commands") is None:
        await bot.add_cog(Commands(bot))
    else:
        print("Commands cog already loaded")
