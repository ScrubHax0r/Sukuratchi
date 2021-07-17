#importing shit
#hi there

from sys import prefix
from discord import message
import json
import nekos
import glob
import discord
from discord.ext import commands
from discord import Embed
from discord.ext.commands import has_permissions, MissingPermissions
import os
from decouple import config
import random
TOKEN = config('TOKEN')

#bot prefix is set here

def get_prefix(client, message):
    with open('prefixes.json', 'r') as f:
        prefixes=json.load(f)
    return prefixes[str(message.guild.id)]
client = commands.Bot(command_prefix=get_prefix)

#variables

#(These variables are useless atm)
#nekoimgs_path = r'C:\\Users\\ScratchHacker\\Documents\\Discord Bot\\NekoImgs'
#nekomimi_list = glob.glob(nekoimgs_path+'*.jpg')
#nekomimi_random = ["neko1.jpg", "neko2.jpg"] (Now useless since I switched to nekoslife api)

#bot commands

@client.event
async def on_ready():
    print("Bot is ready")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="some anime"))

@client.event
async def on_guild_join(guild):
    with open('prefixes.json', 'r') as f:
        prefixes=json.load(f)
    prefixes[str(guild.id)] = '!'
    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@client.event
async def on_guild_remove(guild):
    with open('prefixes.json', 'r') as f:
        prefixes=json.load(f)
    prefixes.pop(str(guild.id))
    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount+1)
    await ctx.send(f'I have deleted {amount} messages, as you requested!', delete_after=5)

@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f'Hey {ctx.message.author.mention}! You don\'t have permission to do that!')

@client.command()
async def setprefix(ctx, prefix):
    with open('prefixes.json', 'r') as f:
        prefixes=json.load(f)
    prefixes[str(ctx.guild.id)] = prefix
    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)
    await ctx.send(f"You have changed the prefix to '{prefix}'!" )

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! Response is at a blazing fast {round(client.latency * 1000)}ms')

@client.command()
async def kemono(ctx):
    await ctx.send('Here\'s a kemonomimi :)')
#This doesn't work atm, trying to figure out why I'm a dumbass.    await ctx.send("Test", nekos.img('kemonomimi'))
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
    await ctx.send(embed=embed)

@client.command()
async def source(ctx):
    await ctx.send('https://github.com/ScrubHax0r/Sukuratchi')

#This gives you a response if you ping the bot
@client.event
async def on_message(message):
    mention = f'{client.user.id}'
    if mention in message.content:
        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)
        prefix = prefixes[str(message.guild.id)]
        await message.channel.send(f"Hi there, {message.author.mention}! I'm Sukuratchi. Do {prefix}help for a list of commands.")
    await client.process_commands(message)

#@client.event
#async def on_message(message):
#    badword = f'Fuck'
#    if badword in message.content:
#        await message.channel.send(f"{message.author.mention} just said a bad word!")
#    await client.process_commands(message)

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
