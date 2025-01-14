import os
import json

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
PREFIX = '!'

CONFIGFILE = {}

with open("./src/config.json", "r") as file:
    CONFIGFILE = json.load(file)


YDL_OPTIONS = {
    'format': 'bestaudio',
    'noplaylist': 'True'
}

YDL_OPTIONS_PLAYLIST_LENGTH = {
    'flatplaylist': 'True',
    'playlistend': 1
}
FFMPEG_OPTIONS = {
    'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
    'options': '-vn'
}

LINK_LIST = [
    'www.youtube.com', 
    'youtube.com', 
    'youtu.be', 
    'www.soundcloud.com', 
    'soundcloud.com'
]

EXTENSIONS_PATH = "src.extensions"

EXTENSIONS = [
    f"{EXTENSIONS_PATH}.{e.replace('.py', '')}"
    for e in os.listdir('./src/extensions') 
    if ".py" in e
]