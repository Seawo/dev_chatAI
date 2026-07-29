from dataclasses import dataclass
from typing import List


@dataclass
class World:

    id: str
    name: str
    location: str
    description: str
    time: str
    weather: str
    current_event: str