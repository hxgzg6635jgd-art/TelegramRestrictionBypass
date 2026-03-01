"""
Logging Configuration Module

Sets up rotating file handler and console logging with configurable format.
Auto-purges log file if it exceeds size limit.

Functions:
    LOGGER: Returns configured logger instance for a given module name
"""

import logging
import os
from logging.handlers import RotatingFileHandler

# Constants
LOG_FILE = "logs.txt"
MAX_LOG_SIZE = 10 * 1024 * 1024  # 10MB
MAX_BYTES_PER_FILE = 5000000  # 5MB per rotating file
BACKUP_COUNT = 10  # Keep 10 backup files

# Ensure log file exists and isn't too huge
if os.path.exists(LOG_FILE):
    if os.path.getsize(LOG_FILE) > MAX_LOG_SIZE:
        os.remove(LOG_FILE)

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(message)s",
    datefmt="%d-%b-%y %I:%M:%S %p",
    handlers=[
        RotatingFileHandler(LOG_FILE, maxBytes=MAX_BYTES_PER_FILE, backupCount=BACKUP_COUNT),
        logging.StreamHandler()
    ]
)


def LOGGER(name: str) -> logging.Logger:
    """
    Get a configured logger instance.

    Args:
        name: Logger name (typically __name__ of the calling module)

    Returns:
        Configured Logger instance
    """
    return logging.getLogger(name)
