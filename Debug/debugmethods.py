from discord.bot import Bot
from discord.ext import commands
from discord.embeds import Embed
import traceback

class DebugMethods(commands.Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    async def reload_cog(self, cogname: str) -> Embed:
        try:
            embeds = self.bot.get_cog("Embeds")
            
            if embeds is not None:
                if cogname is not None:
                    try:
                        self.bot.unload_extension(cogname)
                    except:
                        pass

                    try:
                        self.bot.load_extension(cogname)
                    except:
                        return await embeds.generate_cog_restart_error(cogname)
                    return await embeds.generate_cog_restarted(cogname)
                return await embeds.generate_no_cog_found(cogname)
            
        except Exception as e:
            logging = self.bot.get_cog("Logging")
            if logging is not None:
                await logging.log_error(e,'debugmethods - reload_cog', traceback.format_exc())
            
        if embeds is not None:
            return await embeds.generate_embed_unexpected_error()

    async def cog_status(self) -> Embed:
        try:
            embeds = self.bot.get_cog("Embeds")
            
            if embeds is not None:
                cogcheck:int = 1
                embed: Embed = await embeds.generate_embed("Cog Statuses", "Verifying...", 0xFFFFFF)

                debugcommands = self.bot.get_cog("DebugCommands")
                embeds = self.bot.get_cog("Embeds")
                events = self.bot.get_cog("Events")
                logging = self.bot.get_cog("Logging")

                embed.add_field(name="Debug", value=f"DebugCommands {'🟢' if debugcommands is not None else '🔴' }\nDebugMethods 🟢\nLogging {'🟢' if logging is not None else '🔴' }", inline=False)
                embed.add_field(name="Utilities", value=f"Embeds {'🟢' if embeds is not None else '🔴' }\nEvents {'🟢' if events is not None else '🔴' }", inline=False)
                
                if debugcommands is not None: 
                    cogcheck += 1
                if embeds is not None: 
                    cogcheck += 1
                if events is not None: 
                    cogcheck += 1
                if logging is not None:
                    cogcheck += 1

                embed.description = f"{cogcheck} of 5 cogs working."

                return embed

        except Exception as e:
            if logging is not None:
                await logging.log_error(e, 'debugmethods - cog_status', traceback.format_exc())
            
        if embeds is not None:
            return await embeds.generate_embed_unexpected_error()

def setup(bot):
    bot.add_cog(DebugMethods(bot))