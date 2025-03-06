# Copyright (C) 2025 Hookens
# See the LICENSE file in the project root for details.

from discord import Embed, TextChannel
from discord.activity import Activity
from discord.bot import Bot
from discord.enums import ActivityType
from discord.ext import commands
from discord.member import Member

from Debug.debughelpers import try_func_async
from Utilities.constants import Env, LoggingDefaults

from typing import TYPE_CHECKING, Optional
if TYPE_CHECKING:
    from Debug.logging import Logging
    from Utilities.embeds import Embeds

class Events(commands.Cog):
    def __init__(self, bot: Bot):
        self.bot = bot
    
    async def _handle_member_presence(self, member: Member, joining: bool = True):
        if member.guild.id != Env.GUILD_ID: return
        
        embeds: Optional[Embeds] = self.bot.get_cog("Embeds")
        channel: Optional[TextChannel] = self.bot.get_channel(Env.LOG_CHANNEL)
        if not (embeds and channel): return
        
        embed: Embed = await embeds.generate_embed_member_join(member) if joining else await embeds.generate_embed_member_leave(member)
        await channel.send(embed)

    @commands.Cog.listener()
    @try_func_async()
    async def on_ready (self):
        await self.bot.change_presence(activity=Activity(type=ActivityType.watching, name="the Cattlemen"))

        logging: Logging = self.bot.get_cog("Logging")
        if not logging: return
        
        await logging.log_event(f"{LoggingDefaults.NAME} is up. {len(self.bot.cogs)} of {LoggingDefaults.COG_COUNT} cogs running. Currently serving {len(self.bot.guilds)} servers.", "INFO")


    @commands.Cog.listener()
    @try_func_async()
    async def on_member_join(self, member: Member):
        await self._handle_member_presence(member)
    
    @commands.Cog.listener()
    @try_func_async()
    async def on_member_remove(self, member: Member):
        await self._handle_member_presence(member, False)

def setup(bot):
    bot.add_cog(Events(bot))