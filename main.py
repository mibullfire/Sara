import config # Importamos la configuración del bot. De aquí sacamos el Token y el Prefijo
from config import TOKEN, PREFIX 

import os

import json as jason
import datetime
import asyncio

import time
import discord # La API que hace toda la magia...
from discord.ext import commands

from discord_components import DiscordComponents

from discord_together import DiscordTogether


# Mensajito de postupip install discord-componentreo que indica que se está iniciando:
print(
    "Cargando a Sara, una nueva prueba de mibu en Python <3"
)

# Definición del BOT:
bot = commands.Bot(command_prefix=PREFIX, description='Bot de prueba en Python', intents=discord.Intents.all())

# Abrimos los modulos de la carpeta ./cogs. Aquí guardamos todos los comandos por categorías!
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")

# Eventos de bot:
# Mensaje inicial cuando esté lista, más la actividad.
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="'Fuck the Moon'"))
    print("Sara está lista para la fiesta!")
    DiscordComponents(bot)

# bot.remove_command("help")


@bot.command()
async def ayuda(ctx):
    embed = discord.Embed(title = f"Comandos de Sara ❤️", color = discord.Colour.purple())
    #embed.add_field(name = "ETSII", value = "horario", inline = False)
    #embed.add_field(name = "Imágenes", value = "foxgirl, gasm, gecg, neko, lizard, wallpaper", inline = False)
    embed.add_field(name = "Información", value = "avatar, customavatar, servericon, serverinfo, userinfo", inline = False)
    embed.add_field(name = "Interacción", value = "ambulance, banana, bleed, burn, busy, dance, drink, explosion, fbi, happy, hug, kill, kiss, pat, reverse, run, sad, slap, sleep, wakeup", inline = False)
    embed.add_field(name = "Moderación", value = "ban, kick, purge", inline = False)
    embed.add_field(name = "Utilidad", value = "ball8, coin, dice, say", inline = False)
    embed.add_field(name = "NSFW", value = "ass, bdsm, blowjob, cum, doujin, feet, femdom, foxgirl, glasses, hentai, netorare, maid, masturbation, orgy, panties, pussy, school, succubus, thighs, ugly, uniform, yuri")
    await ctx.send(embed = embed)


# Comandos de los cumpleaños:


bot.run(TOKEN) 