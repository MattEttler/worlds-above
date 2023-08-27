from character import characters
from boundingbox import bounding_boxes
from light import lights
import boundingboxsystem

'''Reset the intensity of lights when they collide with characters.'''


def update_character_light_collisions():
    for i in characters.keys():
        for j in lights.keys():
            if boundingboxsystem.overlaps(
                    bounding_boxes[i],
                    bounding_boxes[j]
                    ):
                lights[j].intensity = 0
