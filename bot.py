import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio

client = discord.Client()

def on_ready():
    print("x77-Bot Started !")

client.run("OTQ2MTE5ODYyOTY5ODI3Mzk5.YhaEyQ.ebzymv65Xrw4Ob6vQtfAUyPXiW4")

await bot.change_presence(activity=discord.Streaming(name="X77-Web.XyZ | The Best DDoS Discord BOT", url=1))

bot = commands.Bot(command_prefix=">")

