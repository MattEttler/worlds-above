from character import characters
from containable import containables
from container import containers
from boundingbox import bounding_boxes
from boundingboxsystem import overlaps

'''Place containables in character inventory upon collision.'''


def update_character_containable_collisions():
    for char_entity in characters.keys():
        # iterate over containables that are on the map
        for containable_entity in (
                bounding_boxes.keys()
                & containables.keys()
                ):
            if overlaps(
                    bounding_boxes[char_entity],
                    bounding_boxes[containable_entity]
                    ):
                # add the containable to the character inventory
                containers[char_entity].entities.add(containable_entity)
                # remove the item from the map
                bounding_boxes.pop(containable_entity, None)
