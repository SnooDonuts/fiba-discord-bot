
import discord
from discord import app_commands
from discord.ext import commands
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import database  # Import database.py
import gamble  # Import gamble.py

class GambleCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="balance", description="Get the balance for a user")
    async def get_balance(self, interaction: discord.Interaction):
        if database.userExists(interaction.user.global_name):
            await interaction.response.send_message(f"Máš {database.checkBalance(interaction.user.global_name)}$")
        else:
            database.createUser(interaction.user.global_name)
            await interaction.response.send_message(f"Počátek cesty pro {interaction.user.global_name} startovací bonus je 100$!!!")

    @app_commands.command(name="maty", description="Defaultní hodnoto pro sázku je 10$")
    async def maty(self, interaction: discord.Interaction, bet: int = 10):
        if database.userExists(interaction.user.global_name) and database.checkBalance(interaction.user.global_name) > bet:
            payout = gamble.maty(bet)
            if payout > 0:
                database.updateBalance(interaction.user.global_name, payout)
                await interaction.response.send_message(f"JO KURWAAA profit")
            else:
                database.updateBalance(interaction.user.global_name, payout)
                await interaction.response.send_message(f"Nemůžeš zkončit na prohře ne more$?!?!?")
        else:
            await interaction.response.send_message(f"Ty se pojeb")


    @app_commands.command(name="ruleta", description="Defaultní hodnoto pro sázku je 10$")
    async def ruleta(self, interaction: discord.Interaction, bet: int = 10, even: bool = False, odd: bool = False, black: bool = False, red: bool = False, low: bool = False, high: bool = False, cum: bool = False):
        if database.userExists(interaction.user.global_name) and database.checkBalance(interaction.user.global_name) > bet:
            payout = gamble.roulette(bet=bet, even=even, odd=odd, black=black, red=red, low=low, high=high, cum=cum)
            if payout > 0:
                database.updateBalance(interaction.user.global_name, payout)
                await interaction.response.send_message(f"JO KURWAAA profit")
            else:
                database.updateBalance(interaction.user.global_name, payout)
                await interaction.response.send_message(f"Nemůžeš zkončit na prohře ne more$?!?!?")
        else:
            await interaction.response.send_message(f"Ty se pojeb")


    @app_commands.command(name="reset", description="Reset user balance")
    async def reset(self, interaction: discord.Interaction):
        database.resetUser(interaction.user.global_name)
        await interaction.response.send_message(f"Balance reset for {interaction.user.global_name}")

async def setup(bot):
    await bot.add_cog(GambleCog(bot))

