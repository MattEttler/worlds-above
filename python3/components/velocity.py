from dataclasses import dataclass


@dataclass
class Velocity():
    x_delta_per_millisecond: int = 0
    y_delta_per_millisecond: int = 0


velocities: dict[Velocity] = {}
