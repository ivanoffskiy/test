import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix=':', self_bot=True, help_command=None)

async def on_ready():
  await client.change_presence(status=discord.Status.online, activity=discord.Game("TESTING"))

client.run(os.getenv("OTU3MDk1OTc2ODkwNDA5MDgw.Yj5zyg.ngGiJrXqbSyfo0VJjueY15FRq0s"), bot=False)
