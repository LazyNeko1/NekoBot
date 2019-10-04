from discord.ext import commands
import discord

prefix = "="

import nbapi

bot = commands.Bot(command_prefix=prefix)



#i have no idea how this works I'll fix it later today 



@bot.command()

async def neko(ctx):

    
    embed=discord.Embed(title='Nekos!')
    embed.set_image(url=nbapi.random.neko())
    await ctx.send(embed=embed)#i have no idea how to make a embed 

    
    
    bot.run('token')
