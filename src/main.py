import logging
import discord
from discord.ext import commands
from dotenv import load_dotenv
import env


load_dotenv()
TOKEN: str = env.getenv("TOKEN")

handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)
@bot.event
async def setup_hook():
    await bot.load_extension("bot_actions.commands")
    await bot.load_extension("bot_actions.events")


bot.run(TOKEN, log_handler=handler, log_level=logging.DEBUG)
