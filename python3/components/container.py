from dataclasses import dataclass


@dataclass
class Container():
    entities: set[int]


containers: dict[Container] = {}
