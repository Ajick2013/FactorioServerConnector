import os


DISCORD_BOT_TOKEN = os.environ.get("DISCORD_BOT_TOKEN", "")
DISCORD_BOT_NAME = os.environ.get("DISCORD_BOT_NAME", "FactorioServerConnector")
DISCORD_MAP_CHANNEL = os.environ.get("DISCORD_MAP_CHANNEL", "")

RCON_ADDR = os.environ.get("RCON_ADDR", "127.0.0.1")
RCON_PORT = os.environ.get("RCON_PORT", "27015")
RCON_PASS = os.environ.get("RCON_PASS", "PASSWORD")

FACTORIO_VOICE_CHANNELS = [
    "Строители",
    "Защитники",
    "Атакующие"
]
FACTORIO_ADMIN_ROLE = "Factorio Server Admin"
USER_MAP_FILE = "user_map.txt"
WHITELIST_FILE = "whitelist.txt"
WHITELIST_POLLING_INTERVAL = 30

user_map = {}
white_list = []
