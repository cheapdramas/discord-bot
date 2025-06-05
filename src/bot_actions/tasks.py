from discord.ext import tasks
from random import randint
import env


TASK_FAILED = "FAILED TO EXECUTE TASK"

class Tasks():
    def __init__(self, bot, voice_channel):
        self.bot = bot
        self.voice_channel = voice_channel

    @tasks.loop(seconds=10)
    async def task_random_sound(self):
        try:
            sounds = self.bot.soundboard_sounds
            random_sound = sounds[randint(0, len(sounds) - 1)]
            await self.voice_channel.send_sound(random_sound)
        except Exception as e:
            print(TASK_FAILED, "task_random_sound", str(e))
    
    async def start(self):
        await self.task_random_sound.start()
