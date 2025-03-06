# Copyright (C) 2025 Hookens
# See the LICENSE file in the project root for details.

from discord import default_permissions
from discord.bot import Bot
from discord.commands import Option
from discord.commands.context import ApplicationContext
from discord.embeds import Embed
from discord.ext import commands
import traceback

COGS = ["Debug.debugcommands", 
        "Debug.debugmethods",
        "Utilities.embeds", 
        "Utilities.events"]

class DebugCommands(commands.Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @commands.slash_command(name="announce", description="Make an announcement embed.", guild_ids=[863766962529632286,])
    @default_permissions(manage_messages=True,)
    async def slash_announce(self, ctx: ApplicationContext, title: Option(str, "Title for the announcement.", required=True), description: Option(str, "Description for the announcement.", required=True)):
        try:
            await ctx.interaction.response.defer(ephemeral=True)

            description = description.replace("\\n", "\n")
            embed: Embed = Embed(title=title, description=description, colour=0xCD6D00)
            embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
            await ctx.channel.send(content="<@&1099830981277532240>", embed=embed)
            await ctx.interaction.followup.send(content="Announcement created.")

        except Exception as e:
            logging = self.bot.get_cog("Logging")
            if logging is not None:
                await logging.log_error(e, 'debugcommands - slash_announce', traceback.format_exc())

    @commands.slash_command(name="shutdown", description="Ends the bot thread.", guild_ids=[858709508561436714,])
    @default_permissions(administrator=True,)
    async def slash_shutdown(self, ctx: ApplicationContext):
        try:
            await ctx.interaction.response.defer(ephemeral=True)
            await ctx.interaction.followup.send(content="Shutting down.")

            exit(1)

        except Exception as e:
            logging = self.bot.get_cog("Logging")
            if logging is not None:
                await logging.log_error(e, 'debugcommands - slash_shutdown', traceback.format_exc())

    @commands.slash_command(name="reload", description="Reload a cog.", guild_ids=[858709508561436714,])
    @default_permissions(administrator=True,)
    async def slash_reload(self, ctx: ApplicationContext, cog: Option(str, "Cog that needs to be reloaded.", choices=COGS, required=True)):
        try:
            await ctx.interaction.response.defer(ephemeral=True)
            
            methods = self.bot.get_cog("DebugMethods")
            if methods is not None:
                await ctx.interaction.followup.send(embed=await methods.reload_cog(cog))

        except Exception as e:
            logging = self.bot.get_cog("Logging")
            if logging is not None:
                await logging.log_error(e, 'debugcommands - slash_reload', traceback.format_exc())
    
    @commands.slash_command(name="status", description="Get bot cogs' status.", guild_ids=[858709508561436714,])
    @default_permissions(administrator=True,)
    async def slash_status(self, ctx: ApplicationContext):
        try:
            await ctx.interaction.response.defer(ephemeral=True)
            
            methods = self.bot.get_cog("DebugMethods")
            if methods is not None:
                await ctx.interaction.followup.send(embed=await methods.cog_status())

        except Exception as e:
            logging = self.bot.get_cog("Logging")
            if logging is not None:
                await logging.log_error(e, 'debugcommands - slash_status', traceback.format_exc())

    @commands.slash_command(name="ping", description="Get bot response time.", guild_ids=[858709508561436714,])
    async def slash_ping(self, ctx: ApplicationContext):
        try:
            await ctx.interaction.response.defer()
            
            embeds = self.bot.get_cog("Embeds")
            if embeds is not None:
                await ctx.interaction.followup.send(embed=await embeds.generate_embed("Pong!", f"Response time: `{int(self.bot.latency*1000)} ms`", 0xFFFFFF))
            
        except Exception as e:
                logging = self.bot.get_cog("Logging")
                if logging is not None:
                    await logging.log_error(e, "debugcommands - slash_ping", traceback.format_exc())
        
        return

def setup(bot):
    bot.add_cog(DebugCommands(bot))