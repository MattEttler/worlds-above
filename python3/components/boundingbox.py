from dataclasses import dataclass

bounding_boxes = {}

@dataclass
class BoundingBox:
    x: int
    y: int
    width: int
    height: int
    outline_size: int = 2 
    red: int = 255
    green: int = 255
    blue: int = 255
