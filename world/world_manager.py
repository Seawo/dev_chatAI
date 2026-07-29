import json
from pathlib import Path

from models.world import World


class WorldManager:

    def __init__(self):

        self.worlds = {}

        self.load_worlds()

    def load_worlds(self):

        folder = Path("data/world")

        print(folder.resolve())   # 추가

        folder.mkdir(parents=True, exist_ok=True)

        for file in folder.glob("*.json"):

            print(file)          # 추가

            try:

                with open(file, "r", encoding="utf-8") as f:
                    data = json.load(f)

                world = World(**data)

                self.worlds[world.id] = world

                print(f"[Loaded] {world.id}")   # 추가

            except Exception as e:
                print(e)

    def get_world(self, world_id):

        return self.worlds.get(world_id)

    def get_all_worlds(self):

        return list(self.worlds.values())

    def reload(self):

        self.worlds.clear()

        self.load_worlds()