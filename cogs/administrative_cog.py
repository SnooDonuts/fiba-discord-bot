
import discord
from discord import app_commands
from discord.ext import commands
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import database  # Import database.py

class administrativeCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="tprint", description="Příkaz pro vypsání TODO")
    async def todoPrint(self, interaction: discord.Interaction):
        pass

    @app_commands.command(name="tadd", description="Příkaz pro přidání položky do TODO. Příklad: /tadd name='Předelat web', prioprity=10, date='12-12-24'")
    async def todoAdd(self, interaction: discord.Interaction, name: str, prioprity: int, date: str, user: str):
        pass

    @app_commands.command(name="trem", description="Příkaz pro odstranění položky do TODO. Příklad: /trem name='Předelat web'")
    async def todoRemove(self, interaction: discord.Interaction, name: str):
        pass

    @app_commands.command(name="tcha", description="Příkaz pro upravení položky v TODO. Příklad: /tcha name='Předelat web', prioprity=8, date='12-11-24'")
    async def todoAdd(self, interaction: discord.Interaction, name: str, prioprity: int, date: str):
        pass

async def setup(bot):
    await bot.add_cog(administrativeCog(bot))

