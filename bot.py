#bot.py

import discord
from discord.ext import commands
import os

#Set debug mode manually
DEBUG = True
#the bot ID
ID = ''

client = commands.Bot(command_prefix='^')

#Initializer function
@client.event
async def on_ready():
    print('bot online')
    if(DEBUG):
        print('-----DEBUG MODE IS ON------')
"""
loads an extension, chose from the following in the cogs folder
Parameters:
    -extension: String which contains the name of the file excluding the extension type
        example: main
"""
@client.command()
async def load(ctx, extension):
    await ctx.send(f'Loading {extension}...')
    client.load_extension(f'cogs.{extension}')
"""
unloads an extension, chose from the following in the cogs folder
Parameters:
    -extension: String which contains the name of the file excluding the extension type
        example: main
"""
@client.command()
async def unload(ctx, extension):
    await ctx.send(f'Unloading {extension}...')
    client.unload_extension(f'cogs.{extension}')

"""
reloads an extension, chose from the following in the cogs folder
Parameters:
    -extension: String which contains the name of the file excluding the extension type
        example: main
"""
@client.command()
async def reload(ctx, extension):
    await ctx.send(f'Reloading {extension}...')
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')

#Generic error handling for missing arguments
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('You are missing arguments in the command, please try again')

#loads all cogs in ./cogs
for filename in os.listdir('./cogs'):
    #only if the file ends in .py
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

#starts the bot
client.run(ID)
