# Copyright (C) 2025 Hookens
# See the LICENSE file in the project root for details.

from datetime import datetime, timedelta
from discord import User
from discord.bot import Bot
from discord.embeds import Embed
from discord.ext import commands
from discord.member import Member
from enum import Enum
import traceback

class Permission(Enum):
    manageroles = 0
    sendmessage = 1
    embedlinks = 2

class Embeds(commands.Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    async def generate_embed(self, title: str, description: str, color: int = 0xCC0000, image: str = None, footer: str = None, **kwargs) -> Embed :
        embed: Embed
        try:
            embed = Embed(title=title, description=description, colour=color)
            if image is not None:
                embed.set_thumbnail(url=image)
            if footer is not None:
                embed.set_footer(text=footer)
                
            for key, value in kwargs.items():
                embed.add_field(name=key, value=value, inline=False)

        except Exception as e:
            logging = self.bot.get_cog("Logging")
            if logging is not None:
                await logging.log_error(e,'embeds - generate_embed', traceback.format_exc(), title, description, color)

        return embed

    async def generate_embed_unexpected_error(self) -> Embed :
        return await self.generate_embed("Unexpected Error", f"Exophose encountered an unexpected error.")


    async def generate_embed_member_join(self, member: Member) -> Embed :
        url = None
        if member.avatar is not None:
            url = member.avatar.url
        return await self.generate_embed(title=f"{member.display_name}", description=f"{member.mention} has joined.", color=0x00CC00, image=url, footer=f"id: {member.id}", Creation=f"<t:{int(member.created_at.timestamp())}:R>")

    async def generate_embed_member_leave(self, member: Member) -> Embed :
        url = None
        if member.avatar is not None:
            url = member.avatar.url
        return await self.generate_embed(title=f"{member.display_name}", description=f"{member.mention} has left.", color=0xCC0000, image=url, footer=f"id: {member.id}", Joined=f"<t:{int(member.joined_at.timestamp())}:R>")


    async def generate_cog_restarted(self, cog: str) -> Embed :
        return await self.generate_embed("Cog Restarted", f"`{cog}` cog was successfully restarted.")

    async def generate_cog_restart_error(self, cog: str) -> Embed :
        return await self.generate_embed("Cog Restart Failed", f"`{cog}` cog could not be restarted.")

    async def generate_no_cog_found(self, cog: str) -> Embed :
        return await self.generate_embed("Cog Not Found", f"`{cog}` cog was not found. Double-check availability.")

def setup(bot):
    bot.add_cog(Embeds(bot))