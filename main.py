#diskoperator by aakaret
#Using discord.py

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import chalk



bot = commands.Bot(command_prefix='+')
@bot.event
async def on_ready():
    print ("READY")
    print ("NAME " + bot.user.name)
    print ("ID " + bot.user.id)
    print ("VER 1.4.2")
    await bot.change_presence(game=discord.Game(name="+h for help"))

@bot.command(pass_context=True)
async def h(ctx):
    embed = discord.Embed(title="Help for DiskOperator", description="+h - Shows help +usri/boti - Info about the user/bot +ready - An Halloween läkerol (swedish candy).", color=0x21bef2)
    await bot.say(embed=embed)
@bot.command(pass_context=True)
async def ready(ctx):
    await bot.say("     **** COMMODORE 65 BASIC V1 ****")
    await bot.say(".")
    await bot.say(" 65k RAM SYSTEM  9/11 BASIC TXTS LEFT  ")
    await bot.say(".")
    await bot.say("READY.")
@bot.command(pass_context=True)
async def boti(ctx):
    embed = discord.Embed(title="Name: DiskOperator", description="Made with :heart: in :flag_se: by @aakare#4977 ", color=0x21bef2)
    embed.set_footer(text="Version 1.3")
    embed.set_author(name="Author: aakaret")
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def usri(ctx, user: discord.Member):
    embed = discord.Embed(title="{}s stats".format(user.name), description="I found this (i hope the info is correct. :fingers_crossed:)", color=0x21bef2)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Join date", value=user.joined_at)
    embed.add_field(name="Rank", value=user.top_role)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)

bot.run("NDI4MTk5NTEyMTQ2OTY4NTc3.DZvnYw.hoNwMC5rbUmXIWseZhGy9zViYPs")
#Please dont steal my money!
