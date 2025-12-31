# Copyright (C) @TheSmartBisnu
# Channel: https://t.me/itsSmartDev

from os import getenv
from time import time
from dotenv import load_dotenv

try:
    load_dotenv("config.env")
except:
    pass

class PyroConf(object):
    API_ID = int(getenv("API_ID", "6"))
    API_HASH = getenv("API_HASH", "eb06d4abfb49dc3eeb1aeb98ae0f581e")
    
    # Support multiple tokens, fallback to single BOT_TOKEN if list unset
    _tokens = getenv("BOT_TOKENS", "")
    BOT_TOKENS = [t.strip() for t in _tokens.split(",")] if _tokens else [getenv("BOT_TOKEN")]
    
    # Validate
    if not BOT_TOKENS[0]:
        print("Error: BOT_TOKENS or BOT_TOKEN must be set.")
        exit(1)
        
    SESSION_STRING = getenv("SESSION_STRING")
    BOT_START_TIME = time()

    MAX_CONCURRENT_DOWNLOADS = int(getenv("MAX_CONCURRENT_DOWNLOADS", "3"))
    BATCH_SIZE = int(getenv("BATCH_SIZE", "10"))
    FLOOD_WAIT_DELAY = int(getenv("FLOOD_WAIT_DELAY", "3"))

