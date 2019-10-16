from discord.ext import commands
import discord

prefix = "#="

import nbapi
from random import randint

bot = commands.Bot(command_prefix=prefix)



#i have no idea how this works I'll fix it later today 



@bot.command()

async def neko(ctx):

    
    embed=discord.Embed(title='Nekos!')
    embed.set_image(url=nbapi.random.neko())
    await ctx.send(embed=embed)#i have no idea how to make a embed 
@bot.command()

async def anime(ctx):

    
    embed=discord.Embed(title='Anime!')
    embed.set_image(url=nbapi.random.anime())
    await ctx.send(embed=embed)#i have no idea how to make a embed 
@bot.command()

async def pat(ctx):

    
    embed=discord.Embed(title='Pats!')
    num = randint(0,1)
    if num == 0:
        embed.set_image(url=nbapi.random.pat.static())
    if num == 1:
        embed.set_image(url=nbapi.random.pat.animated())
    await ctx.send(embed=embed)#i have no idea how to make a embed 

    
    
bot.run('token')
