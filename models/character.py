from dataclasses import dataclass


@dataclass
class Character:

    id: str
    name: str
    age: int
    gender : str 
    relationship: str
    personality: str
    speech_style: str
    description: str