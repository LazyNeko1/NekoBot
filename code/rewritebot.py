from discord.ext import commands
prefix = "#="
import nbapi
bot = commands.Bot(command_prefix=prefix)

#i have no idea how this works I'll fix it later today 

@bot.command()
async def neko(ctx):
    
    await ctx.send(nbapi.random.neko())#i have no idea how to make a embed 
