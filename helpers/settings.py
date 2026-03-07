"""
Settings Management Module

Manages persistent bot configuration and user authorization.
Settings are stored in JSON files and survive bot restarts.

Classes:
    ConfigManager: Persistent configuration manager

Module Variables:
    Config: Singleton ConfigManager instance for global access
"""

import json
import os

# Configuration file paths
SETTINGS_FILE = "downloads/settings.json"
OWNER_FILE = "downloads/owner_id.txt"
DUMP_FILE = "downloads/dump_target.txt"
BOTS_FILE = "downloads/extra_bots.txt"
SOURCE_HISTORY_FILE = "downloads/source_history.json"

# Default configuration values
DEFAULT_SETTINGS = {
    "max_concurrent": 5,
    "flood_delay": 2,
    "authorized_users": [],
    "download_mode": "BOT"
}


class ConfigManager:
    """
    Manages bot configuration with persistence.

    Handles:
    - User authorization (owner and additional users)
    - Download mode (BOT/USER)
    - Performance settings (concurrency, delays)
    - Worker bot tokens
    - Dump channel configuration
    """

    def __init__(self):
        """Initialize configuration manager and load saved settings."""
        self.data = DEFAULT_SETTINGS.copy()
        self.owner_id = None
        self.load()
        if not self.owner_id and os.path.exists(OWNER_FILE):
            try:
                with open(OWNER_FILE, "r") as f:
                    self.owner_id = int(f.read().strip())
            except (ValueError, OSError):
                pass

    def set_owner(self, user_id):
        if not self.owner_id:
            self.owner_id = user_id
            self.ensure_dir()
            with open(OWNER_FILE, "w") as f:
                f.write(str(user_id))
            self.add_user(user_id)

    def load(self):
        if os.path.exists(SETTINGS_FILE):
            try:
                with open(SETTINGS_FILE, "r") as f:
                    saved = json.load(f)
                    self.data.update(saved)
            except (OSError, json.JSONDecodeError):
                pass

    def save(self):
        self.ensure_dir()
        with open(SETTINGS_FILE, "w") as f:
            json.dump(self.data, f, indent=4)

    def ensure_dir(self):
        os.makedirs("downloads", exist_ok=True)

    def get(self, key):
        return self.data.get(key, DEFAULT_SETTINGS.get(key))

    def set(self, key, value):
        self.data[key] = value
        self.save()

    def add_user(self, user_id):
        if user_id not in self.data["authorized_users"]:
            self.data["authorized_users"].append(user_id)
            self.save()

    def remove_user(self, user_id):
        if user_id in self.data["authorized_users"] and user_id != self.owner_id:
            self.data["authorized_users"].remove(user_id)
            self.save()

    def is_authorized(self, user_id):
        return user_id == self.owner_id or user_id in self.data["authorized_users"]

    def get_dump_chat(self):
        if os.path.exists(DUMP_FILE):
            try:
                with open(DUMP_FILE, "r") as f:
                    return int(f.read().strip())
            except (ValueError, OSError):
                return None
        return None

    def set_dump_chat(self, chat_id):
        self.ensure_dir()
        with open(DUMP_FILE, "w") as f: f.write(str(chat_id))

    # --- BOT MANAGEMENT ---
    def get_extra_bots(self):
        if not os.path.exists(BOTS_FILE):
            return []
        try:
            with open(BOTS_FILE, "r") as f:
                return [line.strip() for line in f if line.strip()]
        except OSError:
            return []

    def add_extra_bot(self, token):
        bots = self.get_extra_bots()
        if token not in bots:
            self.ensure_dir()
            with open(BOTS_FILE, "a") as f:
                f.write(f"{token}\n")

    def remove_extra_bot(self, token):
        bots = self.get_extra_bots()
        if token in bots:
            bots.remove(token)
            self.ensure_dir()
            with open(BOTS_FILE, "w") as f:
                if bots:
                    f.write("\n".join(bots) + "\n")
                else:
                    f.write("")

    def clear_dump_chat(self):
        """Clear the destination channel setting."""
        if os.path.exists(DUMP_FILE):
            try:
                os.remove(DUMP_FILE)
            except OSError:
                pass

    # --- SOURCE CHANNEL HISTORY ---
    def get_source_history(self):
        """Get list of recently used source channels."""
        if not os.path.exists(SOURCE_HISTORY_FILE):
            return []
        try:
            with open(SOURCE_HISTORY_FILE, "r") as f:
                data = json.load(f)
                return data.get("history", [])
        except (OSError, json.JSONDecodeError):
            return []

    def add_source_to_history(self, chat_id, chat_title=None):
        """Add a source channel to history (most recent first, max 10)."""
        history = self.get_source_history()

        # Create entry with chat_id and optional title
        entry = {"chat_id": str(chat_id)}
        if chat_title:
            entry["title"] = chat_title

        # Remove if already exists
        history = [h for h in history if h.get("chat_id") != str(chat_id)]

        # Add to front
        history.insert(0, entry)

        # Keep only last 10
        history = history[:10]

        # Save
        self.ensure_dir()
        with open(SOURCE_HISTORY_FILE, "w") as f:
            json.dump({"history": history}, f, indent=4)

Config = ConfigManager()
