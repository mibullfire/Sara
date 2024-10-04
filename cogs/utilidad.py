import discord
from discord.ext import commands
import random

print("Cargados los Comandos de Utilidad")

class utilidad(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
    
    # Comandos

    # Comando para que el bot diga lo que quieras!
    @commands.command()
    async def say(self, ctx, *, response):
        message = ctx.message
        await ctx.send(response)
        await message.delete()
    
    # Comando para lanzar un dado y que salga cara o cruz!
    @commands.command()
    async def coin(self, ctx):
        respuestas = ['cara', 'cruz']
        embed = discord.Embed(description = f'Ha salido **{random.choice(respuestas)}** 🪙!', color = discord.Colour.purple())
        embed.set_thumbnail(url = 'https://c.tenor.com/tewn7lzVDgcAAAAC/coin-flip-flip.gif')
        await ctx.send(embed = embed)
    
    # Comando de Bola 8, haces una pregunta y te responde con varias variables
    @commands.command()
    async def ball8(self, ctx, *, pregunta):
        respuestas = ['Es cierto.', 
        'Es decididamente así.', 
        'Sin duda.', 
        'Sí, definitivamente.', 
        'Puedes confiar en ello.', 
        'Como yo lo veo, sí.', 
        'Probablemente.', 
        'Perspectiva buena.', 
        'Yes!', 
        'Todo apunta a que sí.', 
        'Respuesta confusa, intentalo otra vez.', 
        'Pregunta de nuevo más tarde.', 
        'Mejor no te lo digo ahora.', 
        'No se puede predecir ahora.', 
        'Concéntrate y pregunta otra vez.', 
        'No cuentes con ello.', 
        'Mi respuesta es no.', 
        'Mis fuentes dicen que no.', 
        'Perspectiva no tan buena.', 
        'Muy dudoso']
        embed = discord.Embed(title = f'{ctx.author} pregunta: {pregunta}', description = f'Repuesta: **{random.choice(respuestas)}**', color = discord.Colour.purple())
        embed.set_thumbnail(url = 'https://media1.tenor.com/images/3b766d840bed083e4d809db9a88a58a8/tenor.gif?itemid=10769372')
        await ctx.send(embed = embed)

    # Comando para buscar imágenes en Google:
    @commands.command()
    async def google(seld, ctx, *, google):
        await ctx.send('Error: comando en proceso <3')
    
    @commands.command()
    async def dice(self, ctx):
        numeros = [1, 2, 3, 4, 5, 6]
        embed = discord.Embed(description = f"Ha salido {random.choice(numeros)}!", color = discord.Colour.purple())
        embed.set_thumbnail(url = "https://c.tenor.com/i_L5KauoCcoAAAAi/dice.gif")
        await ctx.send(embed = embed)

    
        
def setup(bot):
    bot.add_cog(utilidad(bot))