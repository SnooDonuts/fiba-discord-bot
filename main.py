
import discord
from discord.ext import commands
import os

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged on as {bot.user}!')
    
    # Automatically load all cogs from the cogs directory
    for filename in os.listdir('./cogs'):
        if filename.endswith('cog.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')
            print(f'Loaded {filename}')
    
    # Sync application commands (slash commands)
    try:
        synced = await bot.tree.sync()
        print(f'Successfully synced {len(synced)} commands.')
    except Exception as e:
        print(f'Failed to sync commands: {e}')

bot.run('')
