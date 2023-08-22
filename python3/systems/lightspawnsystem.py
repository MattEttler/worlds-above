import random
from config import config
import entitymanager
from light import Light, lights
from boundingbox import BoundingBox, bounding_boxes

light_count = config.getint('Lighting', 'LightCount')
width = config.getint('Lighting', 'LightWidth')
height = config.getint('Lighting', 'LightHeight')

'''Reset light entities'''


def spawn_lights(mapSize):
    # always place one light within the fortress.
    fortress_light = entitymanager.create_entity()
    lights[fortress_light] = Light()
    bounding_boxes[fortress_light] = BoundingBox((mapSize/2)-(width/2), (mapSize/2)+(height/2), width, height, 255, 255, 255)
    print(lights.keys())
    # randomly scatter the rest of the lights across the map.
    scattered_lights = {entitymanager.create_entity(): Light() for i in range(light_count-1)}
    lights.update(scattered_lights)
    bounding_boxes.update({entity: BoundingBox(random.randint(0, mapSize), random.randint(0, mapSize), width, height, 255, 255, 255) for entity in scattered_lights.keys()})



def bootstrap_lights(mapSize: int):
    for i in {l for l in lights.keys()}:
        lights.pop(i, None)
        bounding_boxes.pop(i, None)
    spawn_lights(mapSize)
