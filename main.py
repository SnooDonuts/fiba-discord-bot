# main.py
import discord
from discord.ext import commands
from discord import app_commands
import gamble
import database  # Import the new database module

bot = commands.Bot(command_prefix = "!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'Logged on as {bot.user}!')
    await bot.tree.sync()

@bot.event
async def on_message(ctx):
    print(f"{ctx.author.global_name}/{ctx.author.display_name}: {ctx.content}")

@bot.tree.command(name="balance", description="Get the balance for a user")
async def getBalance(interaction: discord.Interaction):
    if database.userExists(interaction.user.global_name):
        await interaction.response.send_message(f"Máš {database.checkBalance(interaction.user.global_name)}$")
    else:
        database.createUser(interaction.user.global_name)
        await interaction.response.send_message(f"Počátek cesty pro {interaction.user.global_name} startovací bonus je 100$!!!")

@bot.tree.command(name="točky", description="TOČKY KURWAAA!!!!!!!!")
async def tocky(interaction: discord.Interaction):
    if database.userExists(interaction.user.global_name) and database.checkBalance(interaction.user.global_name) > 10:
        if gamble.tocky():
            database.updateBalance(interaction.user.global_name, 10)
            await interaction.response.send_message(f"ANO KURWAAA 10$ profit")
        else:
            database.updateBalance(interaction.user.global_name, -10)
            await interaction.response.send_message(f"Nemůžeš zkončit na prohře ne more co -10$?!?!?")
    else:
        await interaction.response.send_message(f"Ty se pojeb")

@bot.tree.command(name='reset')
async def reset(interaction: discord.Interaction):
    database.resetUser(interaction.user.global_name)

bot.run('')
