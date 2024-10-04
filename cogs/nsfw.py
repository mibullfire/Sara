from distutils.log import error
import discord
from discord.ext import commands
import akaneko 

print("Cargados los Comandos de NSFW")

class nsfw(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
    
    # Comandos
    @commands.command()
    async def ass(self, ctx):
        if ctx.channel.is_nsfw():
            imagen = akaneko.nsfw.ass()
            embed = discord.Embed(color = discord.Colour.purple())
            embed.set_image(url = imagen)
            await ctx.send(embed = embed)
        if not ctx.channel.is_nsfw():
            await ctx.send("Este comando muestra imágenes con contenido sexual. Úselo en un chat con NSFW activado :)")
    @commands.command()
    async def bdsm(self, ctx):
        if ctx.channel.is_nsfw():
            imagen = akaneko.nsfw.bdsm()
            embed = discord.Embed(color = discord.Colour.purple())
            embed.set_image(url = imagen)
            await ctx.send(embed = embed)
        if not ctx.channel.is_nsfw():
            await ctx.send("Este comando muestra imágenes con contenido sexual. Úselo en un chat con NSFW activado :)")
    @commands.command()
    async def blowjob(self, ctx):
        if ctx.channel.is_nsfw():
            imagen = akaneko.nsfw.blowjob()
            embed = discord.Embed(color = discord.Colour.purple())
            embed.set_image(url = imagen)
            await ctx.send(embed = embed)
        if not ctx.channel.is_nsfw():
            await ctx.send("Este comando muestra imágenes con contenido sexual. Úselo en un chat con NSFW activado :)")
    @commands.command()
    async def cum(self, ctx):
        if ctx.channel.is_nsfw():
            imagen = akaneko.nsfw.cum()
            embed = discord.Embed(color = discord.Colour.purple())
            embed.set_image(url = imagen)
            await ctx.send(embed = embed)
        if not ctx.channel.is_nsfw():
            await ctx.send("Este comando muestra imágenes con contenido sexual. Úselo en un chat con NSFW activado :)")
    @commands.command()
    async def doujin(self, ctx):
        if ctx.channel.is_nsfw():
            imagen = akaneko.nsfw.doujin()
            embed = discord.Embed(color = discord.Colour.purple())
            embed.set_image(url = imagen)
            await ctx.send(embed = embed)
        if not ctx.channel.is_nsfw():
            await ctx.send("Este comando muestra imágenes con contenido sexual. Úselo en un chat con NSFW activado :)")
    @commands.command()
    async def feet(self, ctx):
        if ctx.channel.is_nsfw():
            imagen = akaneko.nsfw.feet()
            embed = discord.Embed(color = discord.Colour.purple())
            embed.set_image(url = imagen)
            await ctx.send(embed = embed)
        if not ctx.channel.is_nsfw():
            await ctx.send("Este comando muestra imágenes con contenido sexual. Úselo en un chat con NSFW activado :)")
    @commands.command()
    async def femdom(self, ctx):
        if ctx.channel.is_nsfw():
            imagen = akaneko.nsfw.femdom()
            embed = discord.Embed(color = discord.Colour.purple())
            embed.set_image(url = imagen)
            await ctx.send(embed = embed)
        if not ctx.channel.is_nsfw():
            await ctx.send("Este comando muestra imágenes con contenido sexual. Úselo en un chat con NSFW activado :)")
    @commands.command()
    async def foxgirl(self, ctx):
        if ctx.channel.is_nsfw():
            imagen = akaneko.nsfw.foxgirl()
            embed = discord.Embed(color = discord.Colour.purple())
            embed.set_image(url = imagen)
            await ctx.send(embed = embed)
        if not ctx.channel.is_nsfw():
            await ctx.send("Este comando muestra imágenes con contenido sexual. Úselo en un chat con NSFW activado :)")
    @commands.command()
    async def glasses(self, ctx):
        if ctx.channel.is_nsfw():
            imagen = akaneko.nsfw.glasses()
            embed = discord.Embed(color = discord.Colour.purple())
            embed.set_image(url = imagen)
            await ctx.send(embed = embed)
        if not ctx.channel.is_nsfw():
            await ctx.send("Este comando muestra imágenes con contenido sexual. Úselo en un chat con NSFW activado :)")
    @commands.command()
    async def hentai(self, ctx):
        if ctx.channel.is_nsfw():
            imagen = akaneko.nsfw.hentai()
            embed = discord.Embed(color = discord.Colour.purple())
            embed.set_image(url = imagen)
            await ctx.send(embed = embed)
        if not ctx.channel.is_nsfw():
            await ctx.send("Este comando muestra imágenes con contenido sexual. Úselo en un chat con NSFW activado :)")
    @commands.command()
    async def netorare(self, ctx):
        if ctx.channel.is_nsfw():
            imagen = akaneko.nsfw.netorare()
            embed = discord.Embed(color = discord.Colour.purple())
            embed.set_image(url = imagen)
            await ctx.send(embed = embed)
        if not ctx.channel.is_nsfw():
            await ctx.send("Este comando muestra imágenes con contenido sexual. Úselo en un chat con NSFW activado :)")
    @commands.command()
    async def maid(self, ctx):
        if ctx.channel.is_nsfw():
            imagen = akaneko.nsfw.maid()
            embed = discord.Embed(color = discord.Colour.purple())
            embed.set_image(url = imagen)
            await ctx.send(embed = embed)
        if not ctx.channel.is_nsfw():
            await ctx.send("Este comando muestra imágenes con contenido sexual. Úselo en un chat con NSFW activado :)")
    @commands.command()
    async def masturbation(self, ctx):
        if ctx.channel.is_nsfw():
            imagen = akaneko.nsfw.masturbation()
            embed = discord.Embed(color = discord.Colour.purple())
            embed.set_image(url = imagen)
            await ctx.send(embed = embed)
        if not ctx.channel.is_nsfw():
            await ctx.send("Este comando muestra imágenes con contenido sexual. Úselo en un chat con NSFW activado :)")
    @commands.command()
    async def orgy(self, ctx):
        if ctx.channel.is_nsfw():
            imagen = akaneko.nsfw.orgy()
            embed = discord.Embed(color = discord.Colour.purple())
            embed.set_image(url = imagen)
            await ctx.send(embed = embed)
        if not ctx.channel.is_nsfw():
            await ctx.send("Este comando muestra imágenes con contenido sexual. Úselo en un chat con NSFW activado :)")
    @commands.command()
    async def panties(self, ctx):
        if ctx.channel.is_nsfw():
            imagen = akaneko.nsfw.panties()
            embed = discord.Embed(color = discord.Colour.purple())
            embed.set_image(url = imagen)
            await ctx.send(embed = embed)
        if not ctx.channel.is_nsfw():
            await ctx.send("Este comando muestra imágenes con contenido sexual. Úselo en un chat con NSFW activado :)")
    @commands.command()
    async def pussy(self, ctx):
        if ctx.channel.is_nsfw():
            imagen = akaneko.nsfw.pussy()
            embed = discord.Embed(color = discord.Colour.purple())
            embed.set_image(url = imagen)
            await ctx.send(embed = embed)
        if not ctx.channel.is_nsfw():
            await ctx.send("Este comando muestra imágenes con contenido sexual. Úselo en un chat con NSFW activado :)")
    @commands.command()
    async def school(self, ctx):
        if ctx.channel.is_nsfw():
            imagen = akaneko.nsfw.ass()
            embed = discord.Embed(color = discord.Colour.purple())
            embed.set_image(url = imagen)
            await ctx.send(embed = embed)
        if not ctx.channel.is_nsfw():
            await ctx.send("Este comando muestra imágenes con contenido sexual. Úselo en un chat con NSFW activado :)")
    @commands.command()
    async def succubus(self, ctx):
        if ctx.channel.is_nsfw():
            imagen = akaneko.nsfw.succubus()
            embed = discord.Embed(color = discord.Colour.purple())
            embed.set_image(url = imagen)
            await ctx.send(embed = embed)
        if not ctx.channel.is_nsfw():
            await ctx.send("Este comando muestra imágenes con contenido sexual. Úselo en un chat con NSFW activado :)")
    @commands.command()
    async def tentacles(self, ctx):
        if ctx.channel.is_nsfw():
            imagen = akaneko.nsfw.tentacles()
            embed = discord.Embed(color = discord.Colour.purple())
            embed.set_image(url = imagen)
            await ctx.send(embed = embed)
        if not ctx.channel.is_nsfw():
            await ctx.send("Este comando muestra imágenes con contenido sexual. Úselo en un chat con NSFW activado :)")
    @commands.command()
    async def thighs(self, ctx):
        if ctx.channel.is_nsfw():
            imagen = akaneko.nsfw.thighs()
            embed = discord.Embed(color = discord.Colour.purple())
            embed.set_image(url = imagen)
            await ctx.send(embed = embed)
        if not ctx.channel.is_nsfw():
            await ctx.send("Este comando muestra imágenes con contenido sexual. Úselo en un chat con NSFW activado :)")
    @commands.command()
    async def ugly(self, ctx):
        if ctx.channel.is_nsfw():
            imagen = akaneko.nsfw.uglyBastard()
            embed = discord.Embed(color = discord.Colour.purple())
            embed.set_image(url = imagen)
            await ctx.send(embed = embed)
        if not ctx.channel.is_nsfw():
            await ctx.send("Este comando muestra imágenes con contenido sexual. Úselo en un chat con NSFW activado :)")
    @commands.command()
    async def uniform(self, ctx):
        if ctx.channel.is_nsfw():
            imagen = akaneko.nsfw.uniform()
            embed = discord.Embed(color = discord.Colour.purple())
            embed.set_image(url = imagen)
            await ctx.send(embed = embed)
        if not ctx.channel.is_nsfw():
            await ctx.send("Este comando muestra imágenes con contenido sexual. Úselo en un chat con NSFW activado :)")
    @commands.command()
    async def yuri(self, ctx):
        if ctx.channel.is_nsfw():
            imagen = akaneko.nsfw.yuri()
            embed = discord.Embed(color = discord.Colour.purple())
            embed.set_image(url = imagen)
            await ctx.send(embed = embed)
        if not ctx.channel.is_nsfw():
            await ctx.send("Este comando muestra imágenes con contenido sexual. Úselo en un chat con NSFW activado :)")
    @commands.command()
    async def wallpaper(self, ctx):
        if ctx.channel.is_nsfw():
            imagen = akaneko.nsfw.wallpapers()
            embed = discord.Embed(color = discord.Colour.purple())
            embed.set_image(url = imagen)
            await ctx.send(embed = embed)
        if not ctx.channel.is_nsfw():
            await ctx.send("Este comando muestra imágenes con contenido sexual. Úselo en un chat con NSFW activado :)")
        
def setup(bot):
    bot.add_cog(nsfw(bot))