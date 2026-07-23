import json
from pathlib import Path


class MemoryManager:

    def __init__(self):

        self.base_path = Path("data/memories")

        self.base_path.mkdir(parents=True, exist_ok=True)


    def _memory_file(self, player_id, character_id):

        player_folder = self.base_path / player_id

        player_folder.mkdir(parents=True, exist_ok=True)

        return player_folder / f"{character_id}.json"


    def load_memory(self, player_id, character_id):

        file = self._memory_file(player_id, character_id)

        if not file.exists():

            return []

        with open(file, "r", encoding="utf-8") as f:

            data = json.load(f)

        return data["memories"]


    def save_memory(self, player_id, character_id, memories):

        file = self._memory_file(player_id, character_id)

        data = {

            "player_id": player_id,

            "character_id": character_id,

            "memories": memories

        }

        with open(file, "w", encoding="utf-8") as f:

            json.dump(

                data,

                f,

                ensure_ascii=False,

                indent=4

            )


    def add_memory(self, player_id, character_id, memory):

        memories = self.load_memory(

            player_id,

            character_id

        )

        if memory not in memories:

            memories.append(memory)

        self.save_memory(

            player_id,

            character_id,

            memories

        )