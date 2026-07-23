import json
from pathlib import Path

from models.character import Character


class CharacterManager:

    def __init__(self):

        self.characters = {}

        self.load_characters()

    def load_characters(self):

        folder = Path("data/characters")

        if not folder.exists():
            folder.mkdir(parents=True)

        for file in folder.glob("*.json"):

            try:
                with open(file, "r", encoding="utf-8") as f:
                    data = json.load(f)

                character = Character(**data)
                self.characters[character.id] = character

            except json.JSONDecodeError:
                print(f"[WARNING] '{file.name}'은(는) 비어 있거나 JSON 형식이 잘못되었습니다.")

    def get_character(self, character_id):

        return self.characters.get(character_id)

    def get_all_characters(self):

        return list(self.characters.values())

    def reload(self):

        self.characters.clear()

        self.load_characters()