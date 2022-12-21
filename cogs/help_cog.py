#!/usr/bin/env python3

from discord.ext import commands
from src import settings
import discord

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        _prefix = settings.PREFIX
        _embed = settings.EMBED_SETTINGS

        _commands = [
            "p", "s", 
            "loop", "queue", 
            "remove", "pause", 
            "resume", "skipall", 
            "leave", "delete", "help"
        ]

        _final_commands = [
            "**DJ commands**",
            ",".join([f"`{c}`" for c in _commands]),
            "\n",
            f"*Prefix `{_prefix}`*"
        ]

        _embed['description'] = "\n".join(_final_commands)

        self.embed = discord.Embed.from_dict(_embed)
        

    @commands.command(pass_context=True)
    async def help(self, ctx):
        await ctx.send(embed=self.embed)


async def setup(bot):
    await bot.add_cog(Help(bot))
