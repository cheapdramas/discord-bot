from discord.ext import tasks
from discord import FFmpegPCMAudio
from random import randint
from get_random_stuff import random_sound
import config 



TASK_FAILED = "FAILED TO EXECUTE TASK"

class Tasks():
    def __init__(self, bot, voice_channel):
        self.bot = bot
        self.voice_channel = voice_channel

    @tasks.loop(seconds=5)
    async def task_random_sound(self):
        try:
            sound = FFmpegPCMAudio(random_sound())
            self.voice_channel.play(sound)
            print("Playing sound...")
        except Exception as e:
            print(TASK_FAILED, "task_random_sound", str(e))
    
    async def start(self):
        await self.task_random_sound.start()
