"""
State Management Module

Manages batch download progress state for crash-safe auto-resume.
State is persisted to JSON file for recovery after bot restart.

Classes:
    StateManager: Batch progress state manager

Module Variables:
    UserState: Singleton StateManager instance for global access
"""

import json
import os

from logger import LOGGER

# State file path
STATE_FILE = "downloads/user_state.json"


class StateManager:
    """
    Manages per-user batch download state.

    Provides crash-safe batch downloads by persisting progress to disk.
    If the bot crashes during a batch download, it can automatically resume
    from the last saved message ID on restart.
    """

    def __init__(self):
        """Initialize state manager and load saved state."""
        self.data = {}
        self.load()

    def load(self):
        """Load state from JSON file."""
        if os.path.exists(STATE_FILE):
            try:
                with open(STATE_FILE, "r") as f:
                    self.data = json.load(f)
            except Exception as e:
                LOGGER(__name__).error(f"State Load Error: {e}")
                self.data = {}

    def save(self):
        """Save current state to JSON file."""
        try:
            os.makedirs("downloads", exist_ok=True)
            with open(STATE_FILE, "w") as f:
                json.dump(self.data, f, indent=4)
        except Exception as e:
            LOGGER(__name__).error(f"State Save Error: {e}")

    def set_batch(self, user_id: int, source_chat_id, start_id: int, end_id: int):
        """
        Initialize batch download state for a user.

        Args:
            user_id: Telegram user ID
            source_chat_id: Source chat/channel ID
            start_id: Starting message ID
            end_id: Ending message ID
        """
        self.data[str(user_id)] = {
            "source": source_chat_id,
            "start": start_id,
            "end": end_id,
            "current": start_id,
            "status": "active"
        }
        self.save()

    def update_progress(self, user_id: int, current_id: int):
        """
        Update progress for an active batch download.

        Args:
            user_id: Telegram user ID
            current_id: Currently processed message ID
        """
        uid = str(user_id)
        if uid in self.data:
            self.data[uid]["current"] = current_id
            self.save()

    def get_batch(self, user_id: int) -> dict:
        """
        Get batch state for a user.

        Args:
            user_id: Telegram user ID

        Returns:
            Batch state dictionary or None if no active batch
        """
        return self.data.get(str(user_id))

    def clear_batch(self, user_id: int):
        """
        Clear batch state for a user (batch completed or cancelled).

        Args:
            user_id: Telegram user ID
        """
        uid = str(user_id)
        if uid in self.data:
            del self.data[uid]
            self.save()

    def add_single_task(self, user_id: int, source_chat_id, msg_id: int):
        """Add a single download to the persistent queue."""
        uid = str(user_id)
        if "single_tasks" not in self.data:
            self.data["single_tasks"] = {}
        if uid not in self.data["single_tasks"]:
            self.data["single_tasks"][uid] = []

        task = {"source": source_chat_id, "msg_id": msg_id}
        if task not in self.data["single_tasks"][uid]:
            self.data["single_tasks"][uid].append(task)
            self.save()

    def remove_single_task(self, user_id: int, source_chat_id, msg_id: int):
        """Remove a single download from the queue once finished."""
        uid = str(user_id)
        if "single_tasks" in self.data and uid in self.data["single_tasks"]:
            task = {"source": source_chat_id, "msg_id": msg_id}
            if task in self.data["single_tasks"][uid]:
                self.data["single_tasks"][uid].remove(task)
                self.save()


# Singleton instance for global access
UserState = StateManager()
