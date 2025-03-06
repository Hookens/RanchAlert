import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()
TOKENRANCHALERT = os.getenv('DISCORD_TOKEN_RANCHALERT')

intents = discord.Intents().default()
intents.members = True
ranchalertClient = commands.Bot(intents=intents, help_command=None)

ranchalertClient.load_extension("Debug.logging")
ranchalertClient.load_extension("Utilities.events")
ranchalertClient.load_extension("Utilities.embeds")
ranchalertClient.load_extension("Debug.debugcommands")
ranchalertClient.load_extension("Debug.debugmethods")

ranchalertClient.run(TOKENRANCHALERT)