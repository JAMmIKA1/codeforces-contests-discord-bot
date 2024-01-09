import discord
from discord import app_commands
import utils
import os


intents = discord.Intents.all()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)
TOKEN = os.environ.get("DISCORD_TOKEN")


@tree.command(
    name='help',
    description='Displays a list of commands'
)
async def help(interaction):
    commands = tree.get_commands()
    help_text = ""
    for command in commands:
        help_text += f"{command.name}: {command.description}\n"
    await interaction.response.send_message(help_text)


@tree.command(
    name='contests',
    description='Displays a list of upcoming contests'
)
async def contests(interaction):
    await interaction.response.send_message(utils.main())


@client.event
async def on_ready():
    await tree.sync()
    print(f'{client.user} is now running!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel)

    print(f"{username} said: '{user_message}' ({channel})")


client.run(TOKEN)