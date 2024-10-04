import discord
from discord.ext import commands
import random

print("Cargados los Comandos de Interacción")

class interaccion(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
    
    # Comandos
    @commands.command()
    async def ambulance(self, ctx):
        mensaje = []
        image = ['https://j.gifs.com/KRD4n8.gif']

        imagen = random.choice(image)

        embed = discord.Embed(description = f'{ctx.author} llamó a una ambulancia!!', color = discord.Colour.purple())
        embed.set_image(url = imagen)
        await ctx.channel.purge(limit = 1)
        await ctx.send(embed = embed)

    @commands.command()
    async def banana(self, ctx):
        numeros = ['0,00001 nm', '5 cm', '6 cm', '7 cm', '8 cm', '9 cm', '10 cm', '11 cm', '12 cm', '13 cm', '14 cm',
        '15 cm', '16 cm', '17 cm', '18 cm', '19 cm', '20 cm', '21 cm', '22 cm', '23 cm', '24 cm', '25 cm',
        'como la Torre Eiffel', 'como la Torre de Pisa', 'como un cuerno de mamut', 'como una porra']
        palabra = ['El cipote', 'La pinga', 'El titán', 'El aparato reproductor masculino', 'El miembro viril']
        frasecita = ['algo maravilloso', 'algo decepcionante', 'un hecho legendario', 'colosal', 'espectacular', 'un hecho inaudito']

        r_numero = random.choice(numeros)
        r_palabra = random.choice(palabra)
        r_frasecita = random.choice(frasecita)

        embed = discord.Embed(description = f'{r_palabra} de {ctx.author} mide {r_numero}, es simplemente {r_frasecita}.', color = discord.Colour.purple())
        embed.set_image(url = 'https://i.pinimg.com/originals/fb/72/e3/fb72e3b66743496450dd9eb10cd57f7f.jpg')

        await ctx.channel.purge(limit = 1)
        await ctx.send(embed = embed)

    @commands.command()
    async def bleed(self, ctx):
        await ctx.channel.purge(limit = 1)

        mensaje = []
        image = ['https://i.pinimg.com/originals/94/94/33/9494331acecb68a617f3812b6ca7d58c.gif']

        imagen = random.choice(image)

        embed = discord.Embed(description = f'{ctx.author} se desangró... F', color = discord.Colour.purple())
        embed.set_image(url = imagen)
        await ctx.send(embed = embed)

    @commands.command()
    async def burn(self, ctx, member: discord.Member = None):
        await ctx.channel.purge(limit = 1)

        mensaje1 = ['quemó a', 'le prendió fuego a', 'hizo arder a']
        image1 = ['https://c.tenor.com/cSGoc5H-TaoAAAAd/anime-fire-force.gif',
        'https://c.tenor.com/NuasZDvZwM8AAAAC/anime-fire.gif',
        'https://c.tenor.com/dR4RvMWsKfEAAAAC/yukihira-soma-anime.gif',
        'https://c.tenor.com/Bt9BCGE1tvcAAAAC/anime-angry.gif',
        'https://c.tenor.com/0y8yGK559cAAAAAC/flames-twin.gif']

        imagen1 = random.choice(image1)
        Mensaje1 = random.choice(mensaje1)

        mensaje2 = ['está en llamas!!!']

        Mensaje2 = random.choice(mensaje2)

        if member is None:
            embed = discord.Embed(description = f'{ctx.author} {Mensaje2}', color = discord.Colour.purple())
            embed.set_image(url = imagen1)
            
            await ctx.send(embed = embed)
        if member is not None:
            embed = discord.Embed(description = f'{ctx.author} {Mensaje1} {member}', color = discord.Colour.purple())
            embed.set_image(url = imagen1)
            await ctx.send(embed = embed)

    @commands.command()
    async def busy(self, ctx):
        await ctx.channel.purge(limit = 1)
        mensaje = []
        image = ['https://c.tenor.com/RlK21NHtq5UAAAAC/turn-off-shut-off.gif',
        'https://c.tenor.com/33hMyImL9PwAAAAC/busy-frantic.gif',
        'https://c.tenor.com/nXS5cYLmTZcAAAAd/fuck-off-im-busy-im-busy.gif']

        imagen = random.choice(image)

        embed = discord.Embed(description = f'{ctx.author} está ocupado.', color = discord.Colour.purple())
        embed.set_image(url = imagen)
        await ctx.send(embed = embed)

    @commands.command()
    async def dance(self, ctx):
        await ctx.channel.purge(limit = 1)
        mensaje = []
        image = ['https://i.pinimg.com/originals/ed/52/7e/ed527e2e52c51a4138d91c8824530d3e.gif',  
        'https://i.pinimg.com/originals/0b/e4/03/0be4033d4b361127f4990add85864c5e.gif', 
        'https://media1.tenor.com/images/22a0135e7258c3c1a5d1bacfda0a8266/tenor.gif?itemid=10495372', 
        'https://thumbs.gfycat.com/BitesizedQuaintHamadryas-max-1mb.gif', 
        'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/15f74f3c-6be2-454f-bebf-66f618d648c6/d9tw78o-a7f43d47-0636-4b23-af7d-eb386177e13c.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOiIsImlzcyI6InVybjphcHA6Iiwib2JqIjpbW3sicGF0aCI6IlwvZlwvMTVmNzRmM2MtNmJlMi00NTRmLWJlYmYtNjZmNjE4ZDY0OGM2XC9kOXR3NzhvLWE3ZjQzZDQ3LTA2MzYtNGIyMy1hZjdkLWViMzg2MTc3ZTEzYy5naWYifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6ZmlsZS5kb3dubG9hZCJdfQ.ZLLh7_CsFm73gAHvvY_znPhNehSoneKo4lR8K1Act5c', 
        'https://i.kym-cdn.com/photos/images/newsfeed/001/115/816/936.gif',
        'https://i.gifer.com/ICU.gif',
        'https://i.gifer.com/86Tu.gif',
        'https://i.gifer.com/3ww9.gif',
        'https://i.gifer.com/2unv.gif',
        'https://i.gifer.com/8Nwv.gif',
        'https://i.gifer.com/3SfS.gif',
        'https://i.gifer.com/RsVc.gif',
        'https://i.gifer.com/RqUr.gif',
        'https://i.gifer.com/8UYb.gif',
        'https://i.gifer.com/9fjQ.gif',
        'https://i.gifer.com/3yzz.gif',
        'https://i.gifer.com/8Vvs.gif',
        'https://i.gifer.com/YNED.gif']

        imagen = random.choice(image)

        embed = discord.Embed(description = f'{ctx.author} se puso a bailar owo', color = discord.Colour.purple())
        embed.set_image(url = imagen)
        await ctx.send(embed = embed)

    @commands.command()
    async def drink(self, ctx):
        await ctx.channel.purge(limit = 1)

        image = ['https://pa1.narvii.com/6167/e1f8db6aea7e02570e1cfb11183e9a3a4ecbf442_hq.gif',
        'https://c.tenor.com/lFgNDWZT7fkAAAAd/fox-anime.gif']
        mensaje = ['una jarra de cerveza', 'una buena copa de vino', 'un cocacola fresquito',
        'un freeway de limón, siempre operativo', 'una pepsi, y luego la vomitó xD (beban cocacola chicos)', 'una tremenda fanta de naranja']

        imagen = random.choice(image)
        Mensaje = random.choice(mensaje)

        embed = discord.Embed(description = f'{ctx.author} se bebió {Mensaje}.', color = discord.Colour.purple())
        embed.set_image(url = imagen)
        await ctx.send(embed = embed)
    
    @commands.command()
    async def explosion(self, ctx):
        await ctx.channel.purge(limit = 1)     

        mensaje = []
        image = ['https://media1.tenor.com/images/59fe7796250075161bb1937b3a097d21/tenor.gif?itemid=7559841']

        imagen = random.choice(image)

        embed = discord.Embed(description = f'{ctx.author} se volvió un demonio carmesí y explotó el servidor!!', color = discord.Colour.red())
        embed.set_image(url = imagen)
        await ctx.send(embed = embed)


    @commands.command()
    async def fbi(self, ctx, member: discord.Member = None):
        await ctx.channel.purge(limit = 1)

        image1 = ['https://i.pinimg.com/originals/12/13/29/1213293a27c9f84df14051cf37510b41.gif', 
        'https://media1.tenor.com/images/5abcc4434910b37e1c99a38f24a24357/tenor.gif?itemid=17130851']
        image2 = ['https://i.pinimg.com/originals/72/1c/44/721c44173000f30352b8db1fc502f546.gif']

        imagen1 = random.choice(image1)
        imagen2 = random.choice(image2)

        if member is None:
            embed = discord.Embed(description = f'El FBI va a por ti, {ctx.author} huye!!', color = discord.Colour.purple())
            embed.set_image(url = imagen1)
            await ctx.send(embed = embed)
        if member is not None:
            embed = discord.Embed(description = f'{ctx.author} llamó al FBI, {member} correee!!!', color = discord.Colour.purple())
            embed.set_image(url = imagen2)
            await ctx.send(embed = embed)
        
    @commands.command()
    async def happy(self, ctx):
        await ctx.channel.purge(limit = 1)

        mensaje = ['está feliz owo', 'está un viaje de contento jeje', 'está contento >.<']
        image = ['https://media1.tenor.com/images/0f9847a5f258da9a3bdccc3860f91eb5/tenor.gif?itemid=9188246', 
        'https://i.pinimg.com/originals/32/5b/3b/325b3ba6a2beabe21c79b54c6de4e2c7.gif',
        'https://i.gifer.com/Afdn.gif',
        'https://i.gifer.com/Ldb9.gif',
        'https://i.gifer.com/2Vjl.gif',
        'https://i.gifer.com/GmUB.gif',
        'https://i.gifer.com/8gdR.gif',
        'https://i.gifer.com/285U.gif',
        'https://i.gifer.com/6PLh.gif',
        'https://i.gifer.com/7AQ.gif']

        imagen = random.choice(image)
        Mensaje = random.choice(mensaje)

        embed = discord.Embed(description = f'{ctx.author} {Mensaje}', color = discord.Colour.purple())
        embed.set_image(url = imagen)
        await ctx.send(embed = embed)

    @commands.command()
    async def hug(self, ctx, member: discord.Member = None):
        await ctx.channel.purge(limit = 1)
        mensaje1 = ['no mencionó a nadie y le dió un abrazo a un árbol...', 'no dijo a quién abrazar, y abrazó a un árbol xd']
        image1 = ['https://i.gifer.com/CJaE.gif']

        imagen1 = random.choice(image1)
        Mensaje1 = random.choice(mensaje1)

        mensaje2 = ['le dió un abrazo a', 'estrechó entre sus brazos a', 'achuchó a', 'abrazó a', 'le dió un fuerte abrazo a']
        image2 = ['https://media.giphy.com/media/CZpro4AZHs436/giphy.gif',
        'https://media1.tenor.com/images/4ba5c04950f4a7dfc18646d372619212/tenor.gif?itemid=14566836',
        'https://i.pinimg.com/originals/d6/09/ee/d609eeb93489a6418e245b05c2cb0bb1.gif',
        'https://cdn.myanimelist.net/s/common/uploaded_files/1461073447-335af6bf0909c799149e1596b7170475.gif',
        'https://i.kym-cdn.com/photos/images/original/001/184/310/3a3.gif',
        'https://media1.tenor.com/images/0569ee4ea490a197b0b38e92c3eede9e/tenor.gif?itemid=12669025',
        'https://steamuserimages-a.akamaihd.net/ugc/167031784778467223/E4E8FED2B08ECFCEF651F3387A99961586BF0422/', 
        'https://media1.tenor.com/images/b8a6eed08e17e94dad7eada8c63b69f5/tenor.gif?itemid=17363491']

        imagen2 = random.choice(image2)
        Mensaje2 = random.choice(mensaje2)

        if member is None:
            embed = discord.Embed(description = f'{ctx.author} {Mensaje1}', color = discord.Colour.purple())
            embed.set_image(url = imagen1)
            await ctx.send(embed = embed)
        if member is not None:
            embed = discord.Embed(description = f'{ctx.author} {Mensaje2} {member}', color = discord.Colour.purple())
            embed.set_image(url = imagen2)
            await ctx.send(embed = embed)

    @commands.command()
    async def kill(self, ctx, member: discord.Member = None):
        await ctx.channel.purge(limit = 1)
        mensaje1 = ['no tenía ganas de seguir viviendo...', 'eligió el camino más rápido...', 'se suicidó...',
        'hiso la automorisión...', 'se cansó del mundo', 'le dijo adios a su triste vida', 'decidió ser su propio jefe, y fracasó...']
        image1 = ['https://i.pinimg.com/originals/74/eb/31/74eb31df5797673f961814f4cfe24e60.gif', 
        'https://steamuserimages-a.akamaihd.net/ugc/973231127339371847/FCBA72E5FD297925D0C9BC4F51647EC0A218687D/', 
        'https://steamuserimages-a.akamaihd.net/ugc/911288903785421734/EFDDB507FAC574012F636BC73F5BCA1886641BD3/']

        imagen1 = random.choice(image1)
        Mensaje1 = random.choice(mensaje1)

        mensaje2 = ['mató a', 'exterminó a', 'acabó con la vida de', 'eliminó del mundo a']
        image2 = ['https://i.pinimg.com/originals/5d/90/8a/5d908affd86af87bb893864f8c0d38a4.gif']

        imagen2 = random.choice(image2)
        Mensaje2 = random.choice(mensaje2)

        if member is None:
            embed = discord.Embed(description = f'{ctx.author} {Mensaje1}', color = discord.Colour.purple())
            embed.set_image(url = imagen1)
            await ctx.send(embed = embed)
        if member is not None:
            embed = discord.Embed(description = f'{ctx.author} {Mensaje2} {member}', color = discord.Colour.purple())
            embed.set_image(url = imagen2)
            await ctx.send(embed = embed)

    @commands.command()
    async def kiss(self, ctx, member: discord.Member = None):
        await ctx.channel.purge(limit = 1)
        mensaje1 = ['no tiene a nadie a quien besar...', 'no sabe a quien besar...', 'está solito en el mundo...']
        image1 = ['https://i.gifer.com/Hm8L.gif', 
        'https://i.gifer.com/xw3.gif',
        'https://i.gifer.com/NPV4.gif',
        'https://i.gifer.com/Rk5D.gif']

        imagen1 = random.choice(image1)
        Mensaje1 = random.choice(mensaje1)

        mensaje2 = ['le dió un beso a', 'besó a', 'besó apasionadamente y de manera descontrolada y lasciva a', 'le dió un besito a']
        image2 = ['https://i.gifer.com/QPB7.gif',
        'https://i.gifer.com/8Sbz.gif',
        'https://i.gifer.com/PCUi.gif',
        'https://i.gifer.com/C3GK.gif',
        'https://i.gifer.com/2lte.gif',
        'https://i.gifer.com/50Ne.gif',
        'https://i.gifer.com/XJis.gif']

        imagen2 = random.choice(image2)
        Mensaje2 = random.choice(mensaje2)

        if member is None:
            embed = discord.Embed(description = f'{ctx.author} {Mensaje1}', color = discord.Colour.purple())
            embed.set_image(url = imagen1)
            await ctx.send(embed = embed)
        if member is not None:
            embed = discord.Embed(description = f'{ctx.author} {Mensaje2} {member}', color = discord.Colour.purple())
            embed.set_image(url = imagen2)
            await ctx.send(embed = embed)

    @commands.command()
    async def pat(self, ctx, member: discord.Member = None):
        await ctx.channel.purge(limit = 1)
        mensaje1 = [f'Alicia acarició a {ctx.author}']
        image = ['https://i.gifer.com/KJ42.gif',
        'https://i.gifer.com/AWA3.gif',
        'https://i.gifer.com/fybn.gif',
        'https://i.gifer.com/7eXR.gif',
        'https://i.gifer.com/Ckuy.gif',
        'https://i.gifer.com/7eXT.gif',
        'https://i.gifer.com/GJor.gif']

        imagen = random.choice(image)
        Mensaje1 = random.choice(mensaje1)

        mensaje2 = ['acarició a']
        Mensaje2 = random.choice(mensaje2)

        if member is None:
            embed = discord.Embed(description = f'{Mensaje1}', color = discord.Colour.purple())
            embed.set_image(url = imagen)
            await ctx.send(embed = embed)
        if member is not None:
            embed = discord.Embed(description = f'{ctx.author} {Mensaje2} {member}', color = discord.Colour.purple())
            embed.set_image(url = imagen)
            await ctx.send(embed = embed)

    @commands.command()
    async def reverse(self, ctx):
        await ctx.channel.purge(limit = 1)

        mensaje = []
        image = ['https://www.pngitem.com/pimgs/m/511-5111156_uno-reverse-card-gif-hd-png-download.png']

        imagen = random.choice(image)

        embed = discord.Embed(description = f'{ctx.author} usó la carta de los Dioses!', color = discord.Colour.red())
        embed.set_image(url = imagen)
        await ctx.send(embed = embed)
    
    @commands.command()
    async def run(self, ctx, member: discord.Member = None):
        await ctx.channel.purge(limit = 1)

        mensaje1 = ['se puso a correr!', 'se echó a correr!']
        image = ['https://media1.tenor.com/images/0a1aaa016c56cd398a28ba745b541ba8/tenor.gif?itemid=11734758', 
        'https://i.imgur.com/EbMJlcv.gif']

        imagen = random.choice(image)
        Mensaje1 = random.choice(mensaje1)

        mensaje2 = ['huyó de', 'escapó de', 'salió corriendo de']
        Mensaje2 = random.choice(mensaje2)

        if member is None:
            embed = discord.Embed(description = f'{ctx.author} {Mensaje1}', color = discord.Colour.purple())
            embed.set_image(url = imagen)
            await ctx.send(embed = embed)
        if member is not None:
            embed = discord.Embed(description = f'{ctx.author} {Mensaje2} {member}', color = discord.Colour.purple())
            embed.set_image(url = imagen)
            await ctx.send(embed = embed)
    
    @commands.command()
    async def sad(self, ctx):
        await ctx.channel.purge(limit = 1)

        mensaje = ['está triste :(', 'está sad......']
        image = ['https://i.gifer.com/ZjWE.gif',
        'https://i.gifer.com/DO2.gif',
        'https://i.gifer.com/xw3.gif',
        'https://i.gifer.com/AjP.gif',
        'https://i.gifer.com/2mla.gif',
        'https://i.gifer.com/6ElP.gif',
        'https://i.gifer.com/V2Kw.gif',
        'https://i.gifer.com/4N10.gif',
        'https://i.gifer.com/V04k.gif']

        imagen = random.choice(image)
        Mensaje = random.choice(mensaje)

        embed = discord.Embed(description = f'{ctx.author} {Mensaje}', color = discord.Colour.dark_grey())
        embed.set_image(url = imagen)
        await ctx.send(embed = embed)    

    @commands.command()
    async def slap(self, ctx, member: discord.Member = None):
        await ctx.channel.purge(limit = 1)

        mensaje1 = ['Mencione a una víctima :)']
        image = ['https://media1.tenor.com/images/b6d8a83eb652a30b95e87cf96a21e007/tenor.gif?itemid=10426943', 
        'https://media2.giphy.com/media/tX29X2Dx3sAXS/giphy.gif', 
        'https://c.tenor.com/OuYAPinRFYgAAAAC/anime-slap.gifv', 
        'https://i.gifer.com/B2Sm.gif']

        imagen = random.choice(image)
        Mensaje1 = random.choice(mensaje1)

        mensaje2 = ['bofeteó a', 'le metió una ostia a', 'le pegó a']
        Mensaje2 = random.choice(mensaje2)

        if member is None:
            embed = discord.Embed(description = f'{Mensaje1}', color = discord.Colour.purple())
            await ctx.send(embed = embed)
        if member is not None:
            embed = discord.Embed(description = f'{ctx.author} {Mensaje2} {member}', color = discord.Colour.purple())
            embed.set_image(url = imagen)
            await ctx.send(embed = embed)
        
    @commands.command()
    async def sleep(self, ctx):
        await ctx.channel.purge(limit = 1)

        mensaje = []
        image = ['https://media1.tenor.com/images/b190ed9c1cde30f00026433c8b5463ed/tenor.gif?itemid=9340393']

        imagen = random.choice(image)

        embed = discord.Embed(description = f'{ctx.author} se fue a dormir zzzz', color = discord.Colour.purple())
        embed.set_image(url = imagen)
        await ctx.send(embed = embed)

    @commands.command()
    async def wakeup(self, ctx):
        await ctx.channel.purge(limit = 1)

        mensaje = []
        image = ['https://c.tenor.com/gQiYzReiyIAAAAAd/aethestic-anime.gif',
        'https://c.tenor.com/7_bmXy1y1z8AAAAd/anime-gakkougurashi.gif',
        'https://c.tenor.com/UGBvV6dewvsAAAAC/girlsundpanzer-wakeup.gif',
        'https://c.tenor.com/oszhwWfLvgoAAAAd/juliet-persia-juliet.gif',
        'https://c.tenor.com/ao6xrbg47bQAAAAC/morning-wake-up.gif']

        imagen = random.choice(image)

        embed = discord.Embed(description = f'{ctx.author} se acaba de despertar! Buenos días uwu', color = discord.Colour.purple())
        embed.set_image(url = imagen)
        await ctx.send(embed = embed)

  

def setup(bot):
    bot.add_cog(interaccion(bot))