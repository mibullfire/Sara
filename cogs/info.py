import discord
from discord.ext import commands

print("Cargados los Comandos de Información")

class info(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    # Comandos

    # Comando para ver la información del Servidor:
    @commands.command()
    async def serverinfo(self, ctx):
        embed = discord.Embed(title = f"Información de {ctx.guild.name}", color = discord.Colour.purple())
        embed.add_field(name = '🆔 Server ID', value = f"{ctx.guild.id}", inline = True)
        embed.add_field(name = '📆 Fecha de Creación', value = ctx.guild.created_at.strftime("%b %d %Y"), inline = True)
        embed.add_field(name = '👑 Dueño', value = f"{ctx.guild.owner}", inline = True)
        
        embed.add_field(name = '👥 Miembros', value = f'{ctx.guild.member_count} Miembros', inline = True)
        embed.add_field(name = '🌎 Región', value = f'{ctx.guild.region}', inline = True)
        embed.add_field(name = '✅ Verificación', value = f'{ctx.guild.verification_level}', inline = True)

        embed.add_field(name = '🖥 Sistema', value = f'{ctx.guild.system_channel}', inline = True)
        embed.add_field(name = '📜 Reglas', value = f'{ctx.guild.rules_channel}', inline = True)
        embed.add_field(name = '📣 Anuncios', value = f'{ctx.guild.public_updates_channel}', inline = True)

        embed.add_field(name = '⬆️ Nivel', value = f'{ctx.guild.premium_tier}', inline = True)
        embed.add_field(name = '💘 Mejoras', value = f'{ctx.guild.premium_subscription_count} Mejoras', inline = True) 
        embed.add_field(name = '👀 Emojis', value = f'Hasta: {ctx.guild.emoji_limit} Emojis', inline = True)
    

        embed.set_thumbnail(url = ctx.guild.icon_url)  

        await ctx.send(embed=embed)

    # Comando para mostrar la información de un usuario
    @commands.command()
    async def userinfo(self, ctx, member: discord.Member = None):
        if member is None:
            member = ctx.author 

        embed = discord.Embed(title = f'Información de {member.name}', color = discord.Colour.purple())
        embed.set_thumbnail(url = member.avatar_url)
        
        embed.add_field(name = '🚪 Unión:', value = member.joined_at.strftime("%b %d %Y"), inline = True)
        embed.add_field(name = '📣 Actividad', value = member.activity, inline = True)
        embed.add_field(name = '🙋🏻‍♂️ Nickname', value = member.nick)

        embed.add_field(name = '🐙 Server', value = member.guild, inline = True)
        embed.add_field(name = '💎 Nitro', value = member.premium_since.strftime("%b %d %Y"), inline = True)
        embed.add_field(name = '⬆️ Top Rol', value = member.top_role, inline = True)

        return await ctx.send(embed=embed)

    # Comando para mostrar el avatar de un usuario:
    @commands.command()
    async def avatar(self, ctx, member: discord.Member = None):
        if member is None:
            member = ctx.author
        
        embed = discord.Embed(title = f"Avatar de {member.name}", color = discord.Colour.purple())
        embed.set_image(url = member.default_avatar_url)

        await ctx.send(embed = embed)
    
    @commands.command()
    async def customavatar(self, ctx, member: discord.Member = None):
        if member is None:
            member = ctx.author
        
        embed = discord.Embed(title = f'Avatar personalizado de {member.name}', color = discord.Colour.purple())
        embed.set_image(url = member.avatar_url)

        await ctx.send(embed = embed)

    # Comando para mostrar el icono del servidor
    @commands.command()
    async def servericon(self, ctx):
        embed = discord.Embed(title = f"Icono de {ctx.guild.name}!", color = discord.Colour.purple())
        embed.set_image(url = ctx.guild.icon_url)
        await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(info(bot))
