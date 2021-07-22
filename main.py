import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = "§", description = "Bot de Titouan")

@bot.event
async def on_ready():
	print("Ready !")

@bot.command()
async def coucou(ctx):
	print('coucou')
	await ctx.send("Salut !")

bot.run("ODA3MjM0NjIyNzI3MjU4MTMz.YB1B0w.9ZIqBsYc-2BDb1XElcyXNzXmPSE")