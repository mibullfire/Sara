import discord
from discord.ext import commands

print("Cargados los Comandos de Moderación")

class moderacion(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
    
    # Comandos

    # Comando clear
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount=1):
        if amount<50:
            await ctx.channel.purge(limit=amount + 1)
            await ctx.send(f"Se han borrado {amount} mensajes!")
        if amount>50:
            message = ctx.message
            await ctx.send("No se pueden borrar más de 50 mensajes. ¿Por qué? Pues ni idea, mibu no me deja...")
            await message.delete()

    # Comando Ban
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member = None):
        if member is None:
            ctx.send("Debes mencionar a un usuario para banearlo 😈")
        
        await member.ban()
        embed = discord.Embed(color = discord.Colour.purple())
        embed.add_field(name = "Usuario baneado", value = f'{member.name} ha sido banead@')
        await ctx.send(embed=embed)

    # Comando Kick
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member = None):
        if member is None:
            ctx.send("Debes mencionar a un usuario para eliminarlo 😈")
        
        await member.kick()
        embed = discord.Embed(color = discord.Colour.purple())
        embed.add_field(name = "Usuario eliminado", value = f'{member.name} ha sido eliminad@')
        await ctx.send(embed=embed)
        
def setup(bot):
    bot.add_cog(moderacion(bot))