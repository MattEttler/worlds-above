from dataclasses import dataclass

@dataclass
class OxygenTank():
    capacity_m3: int = 0
    volume_m3: int = 0


oxygen_tanks: dict[OxygenTank] = {}
