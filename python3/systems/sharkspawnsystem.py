from config import config
import random
from entitymanager import create_entity
from boundingbox import BoundingBox, bounding_boxes
from velocity import Velocity, velocities

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
    for i in range(COUNT):
        entity = create_entity()
        x_direction = 1 if random.random() < 0.5 else -1
        y_direction = 1 if random.random() < 0.5 else -1
        velocities[entity] = Velocity(
                random.randint(1, BASEMOVEMENTPERSECOND) * x_direction
                / 1000,
                random.randint(1, BASEMOVEMENTPERSECOND) * y_direction
                / 1000
                )
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
