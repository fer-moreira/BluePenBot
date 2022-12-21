import os

PREFIX = '!'

EMBED_SETTINGS = {
    "title": "Mateuzinho bot",
    "description": "aaaaaa",
    "color": 0x0062ff,
    "url": "https://twitter.com/nando_ferreira2",
}

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# self.commands = [
#     "List of commands:",
#     f"{_p}p - Play a song via Youtube/Soundcloud link or search by keywords. If a song is already playing, put the new one in queue.",
#     f"{_p}s - Skip the current song.",
#     f"{_p}loop - Loop the current song.",
#     f"{_p}queue - Show the current queue.",
#     f"{_p}remove - Remove the specified song from the queue (use order number from ,queue).",
#     f"{_p}pause - Pause playback.",
#     f"{_p}resume - Resume playback.",
#     f"{_p}skipall - Empty queue and skip the current song.",
#     f"{_p}leave - Ask the bot to leave the current channel.",
#     f"{_p}delete - Delete the specified amount of bot's messages from the channel (default 10).",
#     f"{_p}help - List the available commands"
# ]