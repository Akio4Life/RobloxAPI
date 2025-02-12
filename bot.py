import discord
from discord.ext import commands
import requests

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

API_URL = "http://yourserver.com/ban"
DISCORD_ADMIN_ROLE = "Admin"

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def setgame(ctx, game_id: str):
    if ctx.author.guild_permissions.administrator:
        with open("config.txt", "w") as f:
            f.write(game_id)
        await ctx.send(f"Game ID set to {game_id}!")
    else:
        await ctx.send("You need admin permissions to run this command.")

bot.run("MTMxODM2NTI5MTkwMTc0NzMwMQ.GvHnpJ.MsTkmds3moMuLekD-DzuMrrPK8r_v4dGHC8aWE")