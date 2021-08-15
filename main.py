import os
import discord
import keep_alive
import datetime
from discord.ext import commands

act = commands.Bot(
    command_prefix='',
    activity=discord.Game(
        application_id=779155175754563624,
        name='Dota 2',
        type=discord.ActivityType.playing,
        start=datetime.datetime.now(),
        assets={'large_image':'dota2'}),
    self_bot=True)

keep_alive.keep_alive()
act.run(os.environ['TOKEN'], bot=False)
