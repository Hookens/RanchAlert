# Copyright (C) 2025 Hookens
# See the LICENSE file in the project root for details.

from discord import ApplicationContext, MessageType, RawReactionActionEvent, TextChannel
from discord.activity import Activity
from discord.bot import Bot
from discord.enums import ActivityType
from discord.ext import commands
from discord.guild import Guild
from discord.member import Member
from discord.message import Message
import traceback

class Events(commands.Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready (self):
        try:
            cogcheck: int = 1
            
            logging = self.bot.get_cog("Logging")
            if logging is not None:
                cogcheck += 1
            if self.bot.get_cog("Embeds") is not None:
                cogcheck += 1
            if self.bot.get_cog("DebugMethods") is not None:
                cogcheck += 1
            if self.bot.get_cog("DebugCommands") is not None:
                cogcheck += 1
            
            await self.bot.change_presence(activity=Activity(type=ActivityType.listening, name="the Cattlemen"))
            
            if logging is not None:
                await logging.log_event(f"RanchAlert is up. {cogcheck} of 5 cogs running.", "INFO")

        except Exception as e:
            if logging is not None:
                await logging.log_error(e,'events - on_ready', traceback.format_exc())
        
        return

    @commands.Cog.listener()
    async def on_member_join(self, member: Member):
        try:
            if member.guild.id == 863766962529632286:
                embeds = self.bot.get_cog("Embeds")
                if embeds is not None:
                    channel: TextChannel = self.bot.get_channel(1099822917036032010)
                    if channel is not None:
                        await channel.send(embed=await embeds.generate_embed_member_join(member))

        except Exception as e:
            logging = self.bot.get_cog("Logging")
            if logging is not None:
                await logging.log_error(e,'events - on_member_join', traceback.format_exc())
        
        return
    
    @commands.Cog.listener()
    async def on_member_remove(self, member: Member):
        try:
            if member.guild.id == 863766962529632286:
                embeds = self.bot.get_cog("Embeds")
                if embeds is not None:
                    channel: TextChannel = self.bot.get_channel(1099822917036032010)
                    if channel is not None:
                        await channel.send(embed=await embeds.generate_embed_member_leave(member))

        except Exception as e:
            logging = self.bot.get_cog("Logging")
            if logging is not None:
                await logging.log_error(e,'events - on_member_remove', traceback.format_exc())
        
        return

def setup(bot):
    bot.add_cog(Events(bot))