class Env:
    API_TOKEN = "" #PUT YOUR API TOKEN HERE
    GUILD_ID = 0 #PUT YOUR GUILD ID HERE
    LOG_CHANNEL = 0 #PUT THE JOIN/LEAVE LOG CHANNEL ID HERE

class LoadOrder:
    COGS = [
        "Debug.logging",
        "Utilities.events",
        "Utilities.embeds",
        "Debug.debugmethods",
        "Debug.debugcommands",
    ]

class LoggingDefaults:
    NAME = "RanchAlert"
    CHANNEL = 0 #PUT YOUR LOG CHANNEL ID HERE
    PING = 0 #PUT YOUR USER ID HERE
    COG_COUNT = len(LoadOrder.COGS)

class EmbedDefaults:
    WHITE = 0xFFFFFF
    GREEN = 0x00CC00
    RED = 0xCC0000
    ORANGE = 0xCD6D00

class DebugLists:
    GUILDS = [
        0, #PUT YOUR DEBUG GUILD ID HERE
    ]

    COGS = [
        "DebugCommands",
        "DebugMethods",
        "Logging",
        "Embeds",
        "Events",
    ]

class DebugTexts:
    C_ANNOUNCE = "Make an announcement embed."
    C_SHUTDOWN = "Ends the bot thread."
    C_RELOAD = "Reload a cog."
    C_STATUS = "Get bot cogs' status."

    F_TITLE = "Title for the announcement."
    F_DESCRIPTION = "Description for the announcement."
    F_COG = "Cog that needs to be reloaded."