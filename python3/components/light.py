from dataclasses import dataclass


@dataclass
class Light():
    intensity: int = 0


lights: dict[Light] = {}
