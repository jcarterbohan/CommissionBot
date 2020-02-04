import discord
from discord.ext import commands

#Set debug mode manually
DEBUG = True

class Twithandler(commands.Cog):

    #initizes client
    def _init_(self, client):
        self.client = client

    #tells when main is ready
    @commands.Cog.listener()
    async def on_ready(self):
        print('twithandler.py started')
        if(DEBUG):
            print('-----DEBUGGING MAIN--------')


    """
    User inputs the twitter name, handle, or URL as an argument
        a message will be displayed showing the webise, prices etc.
    Parameters:
        -handle: A string which contains either a twitter name, handle, or URL
    Exception:
        -if the URL, name, or handle is invalid a message will be returned to the user
    """
    @commands.command()
    async def info(self, ctx, handle):
        await ctx.send('placeholder msg until ready')

#sets up the client variable
def setup(client):
    client.add_cog(Twithandler(client))