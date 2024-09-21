
import discord
from discord import app_commands
from discord.ext import commands
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from database import addTodo, removeTodo, updateTodo, getTodos, createUser, userExists, getAllTodos, getTodoByName

class administrativeCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Command to print the TODO list for a user or for all users if no username is specified
    @app_commands.command(name="tprint", description="Příkaz pro vypsání TODO listu uživatele nebo všech TODO, pokud není zadán uživatel")
    async def todoPrint(self, interaction: discord.Interaction, username: str = None):
        if username:  # If username is provided, print TODO list for that user
            todos = getTodos(username)
            if todos:
                todo_list = "\n".join([f"Name: {name}, Priority: {priority}, Date: {date}" for name, priority, date in todos])
                await interaction.response.send_message(f"TODO list for '{username}':\n{todo_list}")
            else:
                await interaction.response.send_message(f"No TODO items found for user '{username}'.")
        else:  # If no username is provided, print TODO list for all users
            todos = getAllTodos()
            if todos:
                todo_list = "\n".join([f"User: {username}, Name: {name}, Priority: {priority}, Date: {date}" for username, name, priority, date in todos])
                await interaction.response.send_message(f"All TODO items:\n{todo_list}")
            else:
                await interaction.response.send_message("No TODO items found for any user.")

    # Other commands remain unchanged
    @app_commands.command(name="tadd", description="Příkaz pro přidání položky do TODO listu")
    async def todoAdd(self, interaction: discord.Interaction, name: str = "", priority: int = 0, date: str = "", username: str = ""):
        addTodo(name, priority, date, username)
        await interaction.response.send_message(f"TODO item '{name}' added for user '{username}' with priority {priority} and date {date}.")

    @app_commands.command(name="trem", description="Příkaz pro odstranění položky z TODO listu")
    async def todoRemove(self, interaction: discord.Interaction, name: str):
        removeTodo(name)
        await interaction.response.send_message(f"TODO item '{name}' was removed.")

    
    
    @app_commands.command(name="tcha", description="Příkaz pro upravení položky v TODO listu")
    async def todoUpdate(self, interaction: discord.Interaction, name: str = None, priority: int = None, date: str = None, username: str = None):
        # If no name provided, search for the TODO by other parameters
        if name is None:
            todos = getTodos(username=username, date=date, priority=priority)
            if not todos:
                await interaction.response.send_message("No matching TODO items found.")
                return
            # If multiple TODOs match, inform the user
            if len(todos) > 1:
                await interaction.response.send_message(f"Multiple TODO items found: {todos}. Please specify the name to update.")
                return
            # Only one TODO found, use its name for the update
            current_todo = todos[0]
            name = current_todo[0]
        
        # Get the existing TODO if the name is provided
        current_todo = getTodoByName(name)
        if not current_todo:
            await interaction.response.send_message(f"TODO item '{name}' does not exist.")
            return

        # Use current values if no new values are provided
        if priority is None:
            priority = current_todo['priority']
        if date is None:
            date = current_todo['date']
        if username is None:
            username = current_todo['username']
        
        # Update the TODO item with the provided values (or current values if not provided)
        updateTodo(name, priority, date, username)
        await interaction.response.send_message(f"TODO item '{name}' updated for user '{username}' with priority {priority} and date {date}.")



async def setup(bot):
    await bot.add_cog(administrativeCog(bot))

