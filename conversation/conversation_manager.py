import json
from pathlib import Path


class ConversationManager:

    def __init__(self):

        self.base_path = Path("data/conversations")

        self.base_path.mkdir(parents=True, exist_ok=True)

    def _conversation_file(self, player_id, character_id):

        player_folder = self.base_path / player_id

        player_folder.mkdir(parents=True, exist_ok=True)

        return player_folder / f"{character_id}.json"

    def load_conversation(self, player_id, character_id):

        file = self._conversation_file(
            player_id,
            character_id
        )

        if not file.exists():

            return []

        with open(file, "r", encoding="utf-8") as f:

            data = json.load(f)

        return data["messages"]

    def save_conversation(self, player_id, character_id, messages):

        file = self._conversation_file(
            player_id,
            character_id
        )

        data = {
            "messages": messages
        }

        with open(file, "w", encoding="utf-8") as f:

            json.dump(
                data,
                f,
                ensure_ascii=False,
                indent=4
            )

    def add_user_message(self, player_id, character_id, message):

        messages = self.load_conversation(
            player_id,
            character_id
        )

        messages.append(
            {
                "role": "user",
                "content": message
            }
        )

        self.save_conversation(
            player_id,
            character_id,
            messages
        )

    def add_assistant_message(self, player_id, character_id, message):

        messages = self.load_conversation(
            player_id,
            character_id
        )

        messages.append(
            {
                "role": "assistant",
                "content": message
            }
        )

        self.save_conversation(
            player_id,
            character_id,
            messages
        )

    def get_messages(self, player_id, character_id):

        return self.load_conversation(
            player_id,
            character_id
        )

    def clear(self, player_id, character_id):

        self.save_conversation(
            player_id,
            character_id,
            []
        )