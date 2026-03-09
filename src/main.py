import os
from dotenv import load_dotenv
import discord
from discord import app_commands

load_dotenv()

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")
    await tree.sync()

@tree.command(name="ping", description="ping! pong!")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("pong!")

client.run(os.getenv("DISCORD_TOKEN"))
