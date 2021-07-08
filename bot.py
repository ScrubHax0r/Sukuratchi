#importing shit
#hi there

import nekos
import glob
import discord
from discord.ext import commands
from discord import Embed
import os
from decouple import config
import random
TOKEN = config('TOKEN')

#bot prefix is set here

client = commands.Bot(command_prefix = "!")

#variables

nekoimgs_path = r'C:\\Users\\ScratchHacker\\Documents\\Discord Bot\\NekoImgs'
nekomimi_list = glob.glob(nekoimgs_path+'*.jpg')
#nekomimi_random = ["neko1.jpg", "neko2.jpg"] (Now useless since I switched to nekoslife api)

#bot commands

@client.event
async def on_ready():
    print("Bot is ready")

@client.event
async def on_member_join(member):
    print(f'{member} has joined the server')

@client.event
async def on_member_remove(member):
    print(f'{member} has left the server')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! Response is at a blazing fast {round(client.latency * 1000)}ms')

@client.command()
async def kemono(ctx):
    await ctx.send(nekos.img('kemonomimi'))

#HOW I USED TO DO STUFF FOR NEKOS BUT LATER SCRAPPED

#@client.command()
#async def nekofetch(ctx):
#   with open((nekos.cat()), 'rb') as fp:
#        await ctx.send(file=discord.File(fp, 'nekomimi.jpg'))

#bot token is here

client.run(TOKEN)
