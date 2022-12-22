import discord
from src.settings import CONFIGFILE

class GenericEmbed():
    def from_config (self, config):
        return discord.Embed.from_dict(config)
    
    def queue (self, queue, current):
        
        queue_template = CONFIGFILE.get("embeds", {}).get("queue_template", {})
        field_template = queue_template.get('field_template', {})

        embed = self.from_config(queue_template)
        embed.clear_fields()

        for index, song in enumerate(queue):
            embed.add_field(
                inline=field_template.get('inline', False),
                name=field_template.get('name', "\u200B"),
                value=field_template.get('value', "{0} - {1}").format(
                    str(index+1), 
                    song['title']
                ),
            )

        return embed