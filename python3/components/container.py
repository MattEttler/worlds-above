from dataclasses import dataclass


@dataclass
class Container():
    entities: list[int]


containers: dict[Container] = {}
