from dataclasses import dataclass

bounding_boxes = {}

@dataclass
class BoundingBox:
    x: int = 0
    y: int = 0
    width: int = 1
    height: int = 1
    outline_size: int = 2 
    red: int = 255
    green: int = 255
    blue: int = 255
