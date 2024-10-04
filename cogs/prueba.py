import discord
from discord.ext import commands

print("Cargados los Comandos de Prueba")

class prueba(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
    
    # Comandos
    
    @commands.command()
    async def prueba(self, ctx):
        await ctx.send("XD")

    @commands.command()
    async def hola(self, ctx):
        await ctx.send('Hola q tal!')

    @commands.command()
    async def nsfw(sefl, ctx):
        if ctx.channel.is_nsfw():
            await ctx.send("este canal es nsfw")
        if not ctx.channel.is_nsfw():
            await ctx.send("este canal no es nsfw")
   
def setup(bot):
    bot.add_cog(prueba(bot))