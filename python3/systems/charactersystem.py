import random
from config import config
from character import Character, characters
from boundingbox import BoundingBox, bounding_boxes
from entitymanager import create_entity 
from boundingboxsystem import overlaps

# load character configurations
number_of_characters = config.getint('Characters', 'NumberOfCharacters')
starting_max_health = config.getint('Characters', 'CharacterStartingMaxHealth')
width = config.getint('Characters', 'CharacterWidth')
height = config.getint('Characters', 'CharacterHeight')
red = config.getint('Characters', 'CharacterRed')
green = config.getint('Characters', 'CharacterGreen')
blue = config.getint('Characters', 'CharacterBlue')
outline = config.getint('Characters', 'CharacterOutlineSize')
seconds_to_suffocate = config.getint('Characters', 'CharacterSecondsToSuffocate')

def create_character(character: Character, bounding_box: BoundingBox):
    entity = create_entity()    
    characters[entity] = character
    bounding_boxes[entity] = bounding_box

def bootstrap_characters(mapSize):
    for i in range(number_of_characters):
        character = Character(starting_max_health, starting_max_health, 0)
        bounding_box = BoundingBox(random.randint(0, mapSize), random.randint(0, mapSize), width, height, outline, red, green, blue) 
        create_character(character, bounding_box)

def update_characters(fortress: BoundingBox, lapsed_milliseconds: int):
    global characters
    global bounding_boxes
    for i in characters.keys():
        character = characters[i]
        character_box = bounding_boxes[i]
        damage_per_millisecond = character.maxHealth / seconds_to_suffocate / 1000
        if(character.health > 0 and not overlaps(fortress, character_box)):
            character.health = max(0, character.health - (lapsed_milliseconds * damage_per_millisecond))
        character_box.red = 255 - ((255 / character.maxHealth) * (character.maxHealth - character.health))
