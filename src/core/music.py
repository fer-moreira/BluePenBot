import discord
import asyncio
from yt_dlp import YoutubeDL
from src import settings
from discord.ext import commands
from src.utils.message import GenericEmbed
import random


class MusicPlayer:
    def __init__(self, bot):
        self.bot = bot
        self.queue = []
        self.playing = False
        self.loop = False
        self.current_song = None
        self.voice_channel = None
        self.MAX_PER_QUEUE = 10
        
        self.embeds = settings.CONFIGFILE.get("embeds", {})

    def __generate_song (self, results):
        return {
            'title'       : results['title'],
            'source'      : results['url'], 
            'uploader'    : results['uploader'],
            'thumbnail'   : results['thumbnail'],
            'webpage_url' : results['webpage_url']
        }
    
    def __is_valid (self, url):
        pieces = url.split('/')
        _valid = (len(list(set(pieces) & set(settings.LINK_LIST))) > 0)
        return _valid

    def __is_playlist(self, url):
        pieces = url.split("/")
        parameter = pieces[-1].split('?')
        return parameter[0] == 'playlist'

    async def search(self, video, ctx):
        is_link = self.__is_valid(video)
        is_playlist = self.__is_playlist(video)

        if is_playlist:
            asyncio.create_task(self.load_playlist(ctx, video))
        else:
            results = {}
            _link = None

            # Get direct video url or text search
            if is_link: _link = video
            else: _link = f'ytsearch:{video}'

            # Run code inside bot thread
            source = await self.bot.loop.run_in_executor(
                None, self.get_info, settings.YDL_OPTIONS, _link
            )
            
            # Get first video from playlist
            if _link: results = source
            else: results = source.get("entries", [{}])[0]
            
            song = self.__generate_song(results)
            self.queue.append(song)

    async def play_music(self, ctx):
        if len(self.queue) > 0 or self.loop:
            self.playing = True

            if not self.loop:
                self.current_song = self.queue[0]
                await self.send_current_song(ctx)
                self.queue.pop(0)
            
            self.voice_channel.play(
                discord.FFmpegPCMAudio(
                    self.current_song['source'], 
                    **settings.FFMPEG_OPTIONS
                ),
                after = lambda x: asyncio.run_coroutine_threadsafe(self.play_music(ctx), self.bot.loop)
            )

        elif len(self.queue) == 0 or not self.voice_channel.is_playing():
            self.playing = False
            ctx.send("ACABOU AS MUSICA PORRA")
            
    async def load_playlist(self, ctx, link):
        songs = []
        source = await self.bot.loop.run_in_executor(
            None, 
            self.get_info, settings.YDL_OPTIONS_PLAYLIST_LENGTH,
            link
        )
        playlist_length = source['playlist_count']
        for i in range(playlist_length):
            source = await self.bot.loop.run_in_executor(
                None,
                self.get_info,
                {
                    'format': 'bestaudio',
                    'noplaylist': 'False',
                    'playliststart': i+1,
                    'playlistend': i+1
                }, 
                link
            )
            results = source['entries'][0]
            song = self.__generate_song(results)
            self.queue.append(song)
            songs.append(song)
            if not self.playing:
                await self.play_music(ctx)

    async def send_current_song(self, ctx):
        song_info = self.queue[0]
        _settings = self.embeds.get("now_playing", {})

        _settings["fields"][0]["name"]  = song_info['uploader']
        _settings["fields"][0]["value"] = song_info['title']
        _settings["thumbnail"]["url"]   = song_info['thumbnail']

        message = GenericEmbed().from_config(_settings)
        await ctx.send(embed=message)

    @staticmethod
    def get_info(parameters, link):
        return YoutubeDL(parameters).extract_info(link, download=False)

