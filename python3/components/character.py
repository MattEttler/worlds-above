import character 
from dataclasses import dataclass

characters = {}

@dataclass
class Character:
    health: int = 100
    maxHealth: int = 100
    oxygenTankCount: int = 0
    x: int = 0
    y: int = 0

