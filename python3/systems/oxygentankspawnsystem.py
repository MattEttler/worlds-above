from config import config
import random
from entitymanager import create_entity
from oxygentank import OxygenTank, oxygentanks
from boundingbox import BoundingBox, bounding_boxes
from containable import Containable, containables

COUNT = config.getint('OXYGEN', 'O2TankCount')
CAPACITY_M3 = config.getint('OXYGEN', 'O2TankCapacityM3')
WIDTH = config.getint('OXYGEN', 'O2TankWidth')
HEIGHT = config.getint('OXYGEN', 'O2TankHeight')
OUTLINE_SIZE = config.getint('OXYGEN', 'O2TankOutlineSize')
RED = config.getint('OXYGEN', 'O2TankRed')
GREEN = config.getint('OXYGEN', 'O2TankGreen')
BLUE = config.getint('OXYGEN', 'O2TankBlue')


'''Spawn oxygen tanks'''


def spawn_oxygen_tanks(mapSize: int):
    for i in range(COUNT):
        entity = create_entity()
        oxygentanks[entity] = OxygenTank(CAPACITY_M3)
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
        containables[entity] = Containable()


'''Clear out all o2 tanks and respawn new ones.'''


def bootstrap_oxygen_tanks(mapSize):
    for i in {t for t in oxygentanks.keys()}:
        oxygentanks.pop(i, None)
        bounding_boxes.pop(i, None)
    spawn_oxygen_tanks(mapSize)
