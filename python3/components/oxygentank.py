from dataclasses import dataclass

@dataclass
class OxygenTank():
    capacity_m3: int = 0


oxygentanks: dict[OxygenTank] = {}
