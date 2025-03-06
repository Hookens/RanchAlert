# Copyright (C) 2025 Hookens
# See the LICENSE file in the project root for details.

from discord.bot import Bot
from discord.embeds import Embed
from discord.ext import commands
from discord.member import Member

from Utilities.constants import EmbedDefaults

class Embeds(commands.Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    def generate_embed(self, title: str, description: str, color: int = EmbedDefaults.RED, image: str = None, footer: str = None, **kwargs) -> Embed:
        embed = Embed(title=title, description=description, colour=color)
        if image is not None:
            embed.set_thumbnail(url=image)
        if footer is not None:
            embed.set_footer(text=footer)
            
        for key, value in kwargs.items():
            embed.add_field(name=key, value=value, inline=False)

        return embed

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

    #Debug
    def cog_restarted(self, cog: str) -> Embed:
        return self.generate_embed("Cog Restarted", f"`{cog}` cog was successfully restarted.", color=EmbedDefaults.GREEN)

    def cog_restart_error(self, cog: str) -> Embed:
        return self.generate_embed("Cog Restart Failed", f"`{cog}` cog could not be restarted.")


def setup(bot):
    bot.add_cog(Embeds(bot))