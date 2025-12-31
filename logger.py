import logging
import os
from logging.handlers import RotatingFileHandler

# Ensure log file exists and isn't too huge
if os.path.exists("logs.txt"):
    if os.path.getsize("logs.txt") > 10 * 1024 * 1024: # 10MB Limit
        os.remove("logs.txt")

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(message)s",
    datefmt="%d-%b-%y %I:%M:%S %p",
    handlers=[
        RotatingFileHandler("logs.txt", maxBytes=5000000, backupCount=10),
        logging.StreamHandler()
    ]
)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
