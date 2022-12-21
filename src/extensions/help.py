#!/usr/bin/env python3

from discord.ext import commands
from src.settings import CONFIGFILE
from src.utils.message import GenericEmbed

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.embeds = CONFIGFILE.get("embeds", {})

    def main_help(self):
        help_config = self.embeds.get("help", {})
        
        message = GenericEmbed().configure(help_config)
        return message

    @commands.command(pass_context=True)
    async def help(self, ctx, *args):
        message = self.main_help()
        await ctx.send(embed=message)


async def setup(bot):
    await bot.add_cog(Help(bot))
