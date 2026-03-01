# Copyright (C) @TheSmartBisnu
# Channel: https://t.me/itsSmartDev

from os import getenv
from time import time
from dotenv import load_dotenv

try:
    load_dotenv("config.env")
except Exception:
    pass

class PyroConf(object):
    # Validate API_ID
    _api_id = getenv("API_ID", "6")
    try:
        API_ID = int(_api_id)
    except ValueError:
        print(f"Error: API_ID must be a numeric value, not '{_api_id}'")
        print("Please edit config.env and set API_ID to your numeric API ID from my.telegram.org")
        exit(1)

    # Validate API_HASH
    API_HASH = getenv("API_HASH", "eb06d4abfb49dc3eeb1aeb98ae0f581e")
    if API_HASH in ["YOUR_API_HASH_HERE", "eb06d4abfb49dc3eeb1aeb98ae0f581e"]:
        print("Error: API_HASH is not configured properly.")
        print("Please edit config.env and set API_HASH to your API Hash from my.telegram.org")
        exit(1)
    
    # Support multiple tokens, fallback to single BOT_TOKEN if list unset
    _tokens = getenv("BOT_TOKENS", "")
    BOT_TOKENS = [t.strip() for t in _tokens.split(",")] if _tokens else [getenv("BOT_TOKEN")]

    # Validate BOT_TOKENS
    if not BOT_TOKENS[0] or BOT_TOKENS[0] in ["YOUR_BOT_TOKEN_HERE", "None"]:
        print("Error: BOT_TOKENS or BOT_TOKEN must be set to a valid bot token.")
        print("Get a bot token from @BotFather on Telegram and add it to config.env")
        exit(1)
        
    SESSION_STRING = getenv("SESSION_STRING")

    # Warn about SESSION_STRING placeholder
    if SESSION_STRING in ["YOUR_SESSION_STRING_HERE", None, ""]:
        print("Warning: SESSION_STRING is not configured.")
        print("The bot will run in BOT-only mode. To enable USER mode for accessing")
        print("restricted content, generate a session string and add it to config.env")
        SESSION_STRING = None

    BOT_START_TIME = time()

    MAX_CONCURRENT_DOWNLOADS = int(getenv("MAX_CONCURRENT_DOWNLOADS", "3"))
    BATCH_SIZE = int(getenv("BATCH_SIZE", "10"))
    FLOOD_WAIT_DELAY = int(getenv("FLOOD_WAIT_DELAY", "3"))

