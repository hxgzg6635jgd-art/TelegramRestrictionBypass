"""
File Operations Helper Module

Handles file path management, size validation, cleanup, and formatting utilities.

Functions:
    - get_download_path: Create and return safe download paths with UTF-8 handling
    - cleanup_download: Remove downloaded files and empty directories
    - get_readable_file_size: Format bytes into human-readable sizes
    - get_readable_time: Format seconds into human-readable time strings
    - fileSizeLimit: Validate file size against Telegram limits
"""

import os
import shutil
from typing import Optional

from logger import LOGGER

# Constants
SIZE_UNITS = ["B", "KB", "MB", "GB", "TB", "PB"]
MAX_FILENAME_BYTES = 245  # Maximum UTF-8 bytes for filename
TELEGRAM_FILE_LIMIT = 2097152000  # 2GB in bytes
TELEGRAM_PREMIUM_FILE_LIMIT = 2 * TELEGRAM_FILE_LIMIT  # 4GB for premium users


def get_download_path(folder_id: int, filename: str, root_dir: str = "downloads") -> str:
    """
    Create a safe download path with UTF-8 byte limit handling.

    Args:
        folder_id: Identifier for the download folder
        filename: Original filename to save
        root_dir: Root directory for downloads (default: "downloads")

    Returns:
        Full path to the download file
    """
    name, ext = os.path.splitext(filename)
    # Truncate filename to stay within filesystem limits
    while len(filename.encode('utf-8')) > MAX_FILENAME_BYTES:
        name = name[:-1]
        filename = name + ext

    folder = os.path.join(root_dir, str(folder_id))
    os.makedirs(folder, exist_ok=True)
    return os.path.join(folder, filename)


def cleanup_download(path: str) -> None:
    """
    Clean up downloaded file and empty parent directory.

    Args:
        path: Path to the file to clean up
    """
    try:
        if os.path.exists(path):
            os.remove(path)
        if os.path.exists(path + ".temp"):
            os.remove(path + ".temp")
        folder = os.path.dirname(path)
        if os.path.isdir(folder) and not os.listdir(folder):
            shutil.rmtree(folder, ignore_errors=True)
    except Exception as e:
        LOGGER(__name__).error(f"Cleanup failed for {path}: {e}")

def get_readable_file_size(size_in_bytes: Optional[float]) -> str:
    """
    Convert bytes to human-readable file size string.

    Args:
        size_in_bytes: Size in bytes (can be None)

    Returns:
        Formatted string like "1.23 MB" or "0B" if invalid
    """
    if size_in_bytes is None or size_in_bytes < 0:
        return "0B"
    for unit in SIZE_UNITS:
        if size_in_bytes < 1024:
            return f"{size_in_bytes:.2f} {unit}"
        size_in_bytes /= 1024
    return "File too large"


def get_readable_time(seconds: int) -> str:
    """
    Convert seconds to human-readable time string.

    Args:
        seconds: Time duration in seconds

    Returns:
        Formatted string like "1d2h30m45s"
    """
    result = ""
    (days, remainder) = divmod(seconds, 86400)
    days = int(days)
    if days:
        result += f"{days}d"
    (hours, remainder) = divmod(remainder, 3600)
    hours = int(hours)
    if hours:
        result += f"{hours}h"
    (minutes, seconds) = divmod(remainder, 60)
    minutes = int(minutes)
    if minutes:
        result += f"{minutes}m"
    seconds = int(seconds)
    result += f"{seconds}s"
    return result


async def fileSizeLimit(file_size: int, message, action_type: str = "download",
                       is_premium: bool = False) -> bool:
    """
    Validate file size against Telegram limits.

    Args:
        file_size: Size of file in bytes
        message: Telegram message object for reply
        action_type: Type of action ("download" or "upload")
        is_premium: Whether user has Telegram Premium

    Returns:
        True if file size is within limits, False otherwise
    """
    max_size = TELEGRAM_PREMIUM_FILE_LIMIT if is_premium else TELEGRAM_FILE_LIMIT
    if file_size > max_size:
        await message.reply("File too large for Telegram limits.")
        return False
    return True
