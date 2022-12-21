import asyncio
import discord
from discord.ext import commands
from src import settings

async def start_bot():
    bot = commands.Bot(
        command_prefix=settings.PREFIX, 
        intents=discord.Intents.all(), 
        help_command=None
    )

    await bot.load_extension('src.extensions.music')
    await bot.load_extension('src.extensions.help')

    return bot

if __name__ == '__main__':
    bot = asyncio.run(start_bot())
    bot.run(settings.DISCORD_TOKEN)
