import os
import json

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
PREFIX = '!'

CONFIGFILE = {}

with open("config.json", "r") as file:
    CONFIGFILE = json.load(file)