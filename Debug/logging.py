from datetime import datetime, timedelta
import discord
from discord.bot import Bot
from discord.ext import commands
from discord.channel import TextChannel
from discord.embeds import Embed

class Logging(commands.Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    async def log_event (self, event: str, type: str) :

        localizeddatetime = datetime.now() - timedelta(hours=4)

        print(f' {type}  [{localizeddatetime.strftime("%m/%d/%Y %H:%M:%S.%f")[:-3]}] - {event}')

        consoleChannel: TextChannel = self.bot.get_channel(910906077669896262)

        await consoleChannel.send(f'```css\r\n[{type[:4]}] | [{localizeddatetime.strftime("%m/%d/%Y %H:%M:%S.%f")[:-3]}] | {event}\r\n```')

    async def log_error (self, error, function, traceback, *args) :

        localizeddatetime = datetime.now() - timedelta(hours=4)

        print(f' ERROR  [{localizeddatetime.strftime("%m/%d/%Y %H:%M:%S.%f")[:-3]}] - RanchAlert encountered {error} in {function}.')

        epoch: int = int(datetime.now().timestamp())

        embed: Embed = discord.Embed(title=f"Error in RanchAlert", description=error, colour=0xCC0000)

        embed.add_field(name="Timestamp", value=f"<t:{epoch}:F>, <t:{epoch}:R>", inline=True)
        embed.add_field(name="Function", value=f"`{function}`", inline=True)
        embed.add_field(name="Traceback", value=f'`{traceback}`', inline=False)
        if len(args) > 0:
            embed.add_field(name="Arguments", value=f'`{args}`', inline=False)

        consoleChannel: TextChannel = self.bot.get_channel(910906077669896262)

        await consoleChannel.send(embed=embed, content="<@320214798640087040>")

def setup(bot):
    bot.add_cog(Logging(bot))