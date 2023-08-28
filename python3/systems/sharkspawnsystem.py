from config import config
import random
from entitymanager import create_entity
from boundingbox import BoundingBox, bounding_boxes
from velocity import Velocity, velocities
from infinitedrifter import InfiniteDrifter, infinite_drifters

COUNT = config.getint('SHARK', 'SharkCount')
WIDTH = config.getint('SHARK', 'SharkWidth')
HEIGHT = config.getint('SHARK', 'SharkHeight')
OUTLINE_SIZE = config.getint('SHARK', 'SharkOutlineSize')
RED = config.getint('SHARK', 'SharkRed')
GREEN = config.getint('SHARK', 'SharkGreen')
BLUE = config.getint('SHARK', 'SharkBlue')
BASEMOVEMENTPERSECOND = config.getint(
        'SHARK',
        'SharkBaseMovementSpeedPerSecond'
        )


'''Spawn Sharks randomly across the map.'''


def spawn_sharks(mapSize: int):
    for i in range(COUNT-len(infinite_drifters)):
        entity = create_entity()
        infinite_drifters[entity] = InfiniteDrifter()
        x_direction = 1 if random.random() < 0.5 else -1
        y_direction = 1 if random.random() < 0.5 else -1
        velocities[entity] = Velocity(
                random.randint(1, BASEMOVEMENTPERSECOND) * x_direction
                / 1000,
                random.randint(1, BASEMOVEMENTPERSECOND) * y_direction
                / 1000
                )
        bounding_boxes[entity] = BoundingBox(
                random.randint(0, WIDTH),
                random.randint(0, HEIGHT),
                WIDTH,
                HEIGHT,
                OUTLINE_SIZE,
                RED,
                GREEN,
                BLUE
                )


'''Respawn sharks that wander off the screen.'''


def despawn_sharks(mapSize: int):
    off_map_sharks = []
    for i in infinite_drifters.keys():
        box = bounding_boxes[i]
        if (
                box.x > mapSize + box.width
                or box.x < box.width * -1
                or box.y > mapSize + box.height
                or box.y < box.height * -1
                ):
            off_map_sharks.append(i)
    delete_components(off_map_sharks)


'''Delete components associated with sharks.'''


def delete_components(entities: list[int]):
    for i in entities:
        del bounding_boxes[i]
        del infinite_drifters[i]
        del velocities[i]
