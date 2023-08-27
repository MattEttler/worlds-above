from config import config
import random
from entitymanager import create_entity
from boundingbox import BoundingBox, bounding_boxes

COUNT = config.getint('SHARK', 'SharkCount')
WIDTH = config.getint('SHARK', 'SharkWidth')
HEIGHT = config.getint('SHARK', 'SharkHeight')
OUTLINE_SIZE = config.getint('SHARK', 'SharkOutlineSize')
RED = config.getint('SHARK', 'SharkRed')
GREEN = config.getint('SHARK', 'SharkGreen')
BLUE = config.getint('SHARK', 'SharkBlue')


'''Spawn Sharks randomly across the map.'''


def spawn_sharks(mapSize: int):
    for i in range(COUNT):
        entity = create_entity()
        bounding_boxes[entity] = BoundingBox(
                random.randint(0, mapSize),
                random.randint(0, mapSize),
                WIDTH,
                HEIGHT,
                OUTLINE_SIZE,
                RED,
                GREEN,
                BLUE
                )
