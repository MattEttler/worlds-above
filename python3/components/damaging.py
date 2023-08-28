from dataclasses import dataclass


@dataclass
class Damaging():
    damage_per_ms: int = 0


damagers: dict[Damaging] = {}
