from discord.ext import commands
from jsonchik import create_json
from bot_actions.tasks import Tasks
from get_random_stuff import random_gif
import env

MAIN_VOICE_CHANNEL_ID = env.getenv("MAIN_VOICE_CHANNEL_ID")
MAX_WARNINGS          : int = env.getenv("MAX_WARN")

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.message_combo = 0

    @commands.Cog.listener()
    async def on_ready(self):
        print("Starting bot...")
        create_json()
        voice_channel = self.bot.get_channel(MAIN_VOICE_CHANNEL_ID)
        tasks = Tasks(self.bot, voice_channel)
        try:
            await voice_channel.connect()
            await tasks.start()
        except Exception as e:
            print("Bot start failed, reason:", str(e))
            exit()

    @commands.Cog.listener()
    async def on_member_join(self, member):
        await member.send(f"дарова хуїла {member.name}")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        self.message_combo += 1

        if "бля" in message.content.lower():
            await message.delete()
            await message.channel.send(f"{message.author.mention} внучок нє матєрісь")

        if self.message_combo == MAX_WARNINGS:
            await message.channel.send(random_gif())
            self.message_combo = 0

        await self.bot.process_commands(message)

async def setup(bot):
    await bot.add_cog(Events(bot))
