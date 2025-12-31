import json
import os
from logger import LOGGER

STATE_FILE = "downloads/user_state.json"

class StateManager:
    def __init__(self):
        self.data = {}
        self.load()

    def load(self):
        if os.path.exists(STATE_FILE):
            try:
                with open(STATE_FILE, "r") as f:
                    self.data = json.load(f)
            except Exception as e:
                LOGGER(__name__).error(f"State Load Error: {e}")
                self.data = {}

    def save(self):
        try:
            os.makedirs("downloads", exist_ok=True)
            with open(STATE_FILE, "w") as f:
                json.dump(self.data, f, indent=4)
        except Exception as e:
            LOGGER(__name__).error(f"State Save Error: {e}")

    def set_batch(self, user_id, source_chat_id, start_id, end_id):
        self.data[str(user_id)] = {
            "source": source_chat_id,
            "start": start_id,
            "end": end_id,
            "current": start_id,
            "status": "active"
        }
        self.save()

    def update_progress(self, user_id, current_id):
        uid = str(user_id)
        if uid in self.data:
            self.data[uid]["current"] = current_id
            self.save()

    def get_batch(self, user_id):
        return self.data.get(str(user_id))

    def clear_batch(self, user_id):
        uid = str(user_id)
        if uid in self.data:
            del self.data[uid]
            self.save()

UserState = StateManager()
