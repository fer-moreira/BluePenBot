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

    for extension in settings.EXTENSIONS:
        print(f"Loading extension: {extension}")
        await bot.load_extension(extension)

    return bot

if __name__ == '__main__':
    bot = asyncio.run(start_bot())
    bot.run(settings.DISCORD_TOKEN)
