#importing shit
#hi there

from discord import message
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

@client.command()
async def easteregg(ctx):
    await ctx.send('Never gonna give you up. Never gonna let you down. Never gonna run around and desert you')

#@client.command()
#async def kemonofetch(ctx):
#    embed = discord.Embed(title=(nekos.img('kemonomimi')), description=(nekos.img('kemonomimi'))) #,color=Hex code
#    embed.add_field(name="Name", value="you can make as much as fields you like to")
#    await ctx.send(embed=embed)

@client.command()
async def kemonofetch(ctx):
    embed = discord.Embed()
    embed.set_image(url=(nekos.img('kemonomimi')))

#@client.command()
#async def stopbot(ctx):
#    await ctx.send('Stoppng the bot')
#    exit()

#HOW I USED TO DO STUFF FOR NEKOS BUT LATER SCRAPPED
#(Also this whole section doesn't even work if I uncomment it, I used to just use files on my pc and used a random module)

#@client.command()
#async def nekofetch(ctx):
#   with open((nekos.cat()), 'rb') as fp:
#        await ctx.send(file=discord.File(fp, 'nekomimi.jpg'))

#bot token is here

client.run(TOKEN)
