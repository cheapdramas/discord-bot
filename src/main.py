import logging
import discord
from discord.ext import commands
import config


TOKEN: str = config.getenv("TOKEN")

handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)
@bot.event
async def setup_hook():
    await bot.load_extension("bot_actions.events")
    await bot.load_extension("bot_actions.commands")


bot.run(TOKEN, log_handler=handler, log_level=logging.DEBUG)
