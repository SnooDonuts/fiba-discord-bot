
import discord
from discord import app_commands
from discord.ext import commands
import database  # Import the database module

class UserCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="balance", description="Get the balance for a user")
    async def get_balance(self, interaction: discord.Interaction):
        username = interaction.user.global_name
        if database.userExists(username):
            balance = database.checkBalance(username)
            await interaction.response.send_message(f"Máš {balance}$")
        else:
            database.createUser(username)
            await interaction.response.send_message(f"Počátek cesty pro {username} startovací bonus je 100$!!!")

    @app_commands.command(name="točky", description="TOČKY KURWAAA!!!!!!!!")
    async def tocky(self, interaction: discord.Interaction):
        username = interaction.user.global_name
        if database.userExists(username) and database.checkBalance(username) > 10:
            if gamble.tocky():  # Assuming `gamble.tocky()` is a valid function
                database.updateBalance(username, 10)
                await interaction.response.send_message(f"ANO KURWAAA 10$ profit")
            else:
                database.updateBalance(username, -10)
                await interaction.response.send_message(f"Nemůžeš zkončit na prohře ne more co -10$?!?!?")
        else:
            await interaction.response.send_message(f"Ty se pojeb")

    @app_commands.command(name="reset", description="Reset the user's balance to 100")
    async def reset(self, interaction: discord.Interaction):
        username = interaction.user.global_name
        database.resetUser(username)
        await interaction.response.send_message(f"{username}, your balance has been reset to 100$!")

async def setup(bot):
    await bot.add_cog(UserCommands(bot))

