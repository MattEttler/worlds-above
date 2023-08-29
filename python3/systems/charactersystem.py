import random
from config import config
from character import Character, characters
from boundingbox import BoundingBox, bounding_boxes
from entitymanager import create_entity, clear_entities
from boundingboxsystem import overlaps
from container import Container, containers
from oxygentank import oxygen_tanks
from meat import Meat, meats

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
o2_consumption_per_second = config.getint('Characters', 'CharacterO2ConsumptionPerSecond')
o2_fill_rate_per_second = config.getint('Fortress', 'FortressO2FillRatePerSecond')


def create_character(character: Character, bounding_box: BoundingBox, container: Container):
    entity = create_entity()
    characters[entity] = character
    bounding_boxes[entity] = bounding_box
    containers[entity] = container
    meats[entity] = Meat()
    return entity


def delete_characters(player_ids={}):
    clear_entities(player_ids)
    for i in {c for c in player_ids}:
        del characters[i]
        del bounding_boxes[i]
        del containers[i]
        del meats[i]


def bootstrap_characters(mapSize):
    delete_characters(characters.keys())
    for i in range(number_of_characters):
        character = Character(starting_max_health, starting_max_health, 0)
        bounding_box = BoundingBox(random.randint(0, mapSize), random.randint(0, mapSize), width, height, outline, red, green, blue) 
        container = Container(set())
        create_character(character, bounding_box, container)


def update_characters(fortress: BoundingBox, lapsed_milliseconds: int):
    global characters
    global bounding_boxes
    for i in characters.keys():
        character = characters[i]
        character_box = bounding_boxes[i]
        damage_per_millisecond = character.maxHealth / seconds_to_suffocate / 1000
        character_o2_volume = sum([
            oxygen_tanks[t].volume_m3 for t in (
                oxygen_tanks.keys()
                & containers[i].entities)
            ])
        character_o2_capacity = sum([
            oxygen_tanks[t].capacity_m3 for t in (
                oxygen_tanks.keys()
                & containers[i].entities)])
        if not overlaps(fortress, character_box):
            if character_o2_volume > 0:
                consume_o2_tanks(
                        i,
                        o2_consumption_per_second / 1000,
                        lapsed_milliseconds)
            if character_o2_volume <= 0 and character.health > 0:
                character.health = max(
                        0,
                        character.health
                        - (lapsed_milliseconds * damage_per_millisecond))
        elif character_o2_volume < character_o2_capacity:
            fill_o2_tanks(
                i,
                o2_fill_rate_per_second / 1000,
                lapsed_milliseconds)
        character_box.red = 255 - ((255 / character.maxHealth) * (character.maxHealth - character.health))


'''Consume o2 tanks'''


def consume_o2_tanks(character_id, o2_consumption_per_millisecond, lapsed_milliseconds):
    non_empty_tanks = [
            oxygen_tanks[tank] for tank in (
                oxygen_tanks.keys()
                & containers[character_id].entities)
            if oxygen_tanks[tank].volume_m3 > 0
            ]
    non_empty_tanks[0].volume_m3 = max(0, non_empty_tanks[0].volume_m3 - (lapsed_milliseconds * o2_consumption_per_millisecond))

'''Fill unused capacity of o2 tanks'''


def fill_o2_tanks(character_id, o2_fill_per_millisecond, lapsed_milliseconds):
    non_full_tanks = [
            oxygen_tanks[tank] for tank in (
                oxygen_tanks.keys()
                & containers[character_id].entities)
            if oxygen_tanks[tank].volume_m3 < oxygen_tanks[tank].capacity_m3
            ]
    non_full_tanks[0].volume_m3 = min(non_full_tanks[0].capacity_m3, non_full_tanks[0].volume_m3 + (lapsed_milliseconds * o2_fill_per_millisecond))
