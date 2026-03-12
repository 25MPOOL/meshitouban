import os
import sys
from dotenv import load_dotenv
import discord
from discord import app_commands

load_dotenv()


class MeshibanClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self) -> None:
        if "--sync-only" in sys.argv:
            print("同期するために起動します")
            await self.tree.sync()
            print("同期しました。終了します。")
            await self.close()
            sys.exit()


intents = discord.Intents.default()
client = MeshibanClient(intents=intents)
tree = client.tree


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@tree.command(name="ping", description="ping! pong!")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("pong!")


client.run(os.getenv("DISCORD_TOKEN"))
