from config import config
from character import characters
from damaging import damagers
from boundingbox import bounding_boxes
from boundingboxsystem import overlaps

'''Place containables in character inventory upon collision.'''


def update_character_damager_collisions(lapsed_milliseconds: int):
    for char_entity in characters.keys():
        # iterate over containables that are on the map
        for damaging_entity in damagers.keys():
            if overlaps(
                    bounding_boxes[char_entity],
                    bounding_boxes[damaging_entity]
                    ):
                # deal damage to the character

                characters[char_entity].health = max(
                        0,
                        characters[char_entity].health
                        - (lapsed_milliseconds * damagers[damaging_entity].damage_per_ms)
                        )
