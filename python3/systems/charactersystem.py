import random
from config import config
from character import Character, characters
from boundingbox import BoundingBox, bounding_boxes
from entitymanager import create_entity 

# load character configurations
number_of_characters = config.getint('Characters', 'NumberOfCharacters')
starting_max_health = config.getint('Characters', 'CharacterStartingMaxHealth')
width = config.getint('Characters', 'CharacterWidth')
height = config.getint('Characters', 'CharacterHeight')
red = config.getint('Characters', 'CharacterRed')
green = config.getint('Characters', 'CharacterGreen')
blue = config.getint('Characters', 'CharacterBlue')
outline = config.getint('Characters', 'CharacterOutlineSize')

def create_character(character: Character, bounding_box: BoundingBox):
    entity = create_entity()    
    characters[entity] = character
    bounding_boxes[entity] = bounding_box

def bootstrap_characters(mapSize):
    for i in range(number_of_characters):
        character = Character(starting_max_health, starting_max_health, 0)
        bounding_box = BoundingBox(random.randint(0, mapSize), random.randint(0, mapSize), width, height, outline, red, green, blue) 
        create_character(character, bounding_box)
