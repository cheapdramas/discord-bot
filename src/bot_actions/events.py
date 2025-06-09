import discord 
from discord.ext import commands
from jsonchik import create_json
from bot_actions.tasks import Tasks
from get_random_stuff import random_gif 
import config 

MAIN_VOICE_CHANNEL_ID: int = config.getenv("MAIN_VOICE_CHANNEL_ID")
MAX_WARNINGS: int = config.getenv("MAX_WARNINGS")

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.message_combo = 0
        #changing immediately when bot starts (on_ready)
        self.voice_client: None | discord.VoiceClient = None

    @commands.Cog.listener()
    async def on_ready(self):
        print("Starting bot...")
        create_json()
        voice_channel = self.bot.get_channel(MAIN_VOICE_CHANNEL_ID)
        try:
            self.voice_client = await voice_channel.connect()
            tasks = Tasks(self.bot, self.voice_client)
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

        if self.message_combo == 5:
            await message.channel.send(random_gif())
            self.message_combo = 0
            print("MESSAGE COMBO! Sending gif..")
        
        if self.bot.user in message.mentions:
            content = message.content.lower()
            #@BOT no sound = досить грати звук у войс каналі
            if "no sound" in content:
                if self.voice_client.is_playing():
                    self.voice_client.stop()
                    await message.channel.send(f"{message.author.mention} ти заїбав")
                    


        await self.bot.process_commands()

async def setup(bot):
    if bot.get_cog("Events") is None:
        await bot.add_cog(Events(bot))
    else:
        print("Commands cog already loaded")

