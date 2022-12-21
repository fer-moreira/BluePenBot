import discord

class GenericEmbed():
    def configure (self, config):
        return discord.Embed.from_dict(config)