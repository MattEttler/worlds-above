import math
from config import config
import pygame
from character import Character, characters
from boundingbox import BoundingBox, bounding_boxes
from container import Container, containers
from oxygentank import oxygen_tanks
import charactersystem
import entitymanager
import gamestatemanager

# load character configurations.
# TODO: compress this into a common area with the CharacterCreationSystem
width = config.getint('Characters', 'CharacterWidth')
height = config.getint('Characters', 'CharacterHeight')

def bootstrap(mapSize: int):
    playerCharacter = Character()
    playerBox = BoundingBox()
    playerBox.width = width
    playerBox.height = height
    playerBox.red = 255
    playerBox.blue = 255
    playerBox.green = 0
    playerBox.outline_size = 0
    playerBox.x = mapSize/2
    playerBox.y = mapSize/2
    playerInventory = Container(set())
    return charactersystem.create_character(
            playerCharacter,
            playerBox,
            playerInventory
            )


base_movement_speed_per_second = config.getint(
        'Player',
        'PlayerBaseMovementSpeedPerSecond')
base_movement_speed_per_millisecond = base_movement_speed_per_second / 1000

'''Process logical updates for a particular player.'''


def update_player(player_id: int, lapsed_milliseconds: int):
    global bounding_boxes
    player_box = bounding_boxes[player_id]
    player_character = characters[player_id]
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_box.x = player_box.x - (base_movement_speed_per_millisecond * lapsed_milliseconds)
    if keys[pygame.K_RIGHT]:
        player_box.x = player_box.x + (base_movement_speed_per_millisecond * lapsed_milliseconds)
    if keys[pygame.K_UP]:
        player_box.y = player_box.y - (base_movement_speed_per_millisecond * lapsed_milliseconds)
    if keys[pygame.K_DOWN]:
        player_box.y = player_box.y + (base_movement_speed_per_millisecond * lapsed_milliseconds)

    if player_character.health <= 0:
        gamestatemanager.game_state = gamestatemanager.GameState.OVER


'''Render the heads up display for a particular player.'''


def render_hud(player_id, font, screen):
    player_character = characters[player_id]
    player_o2_tanks = (
            containers[player_id].entities
            & oxygen_tanks.keys()
            )
    oxygen_capacity_m3 = sum([oxygen_tanks[tank].capacity_m3 for tank in player_o2_tanks])
    oxygen_volume_m3 = sum([oxygen_tanks[tank].volume_m3 for tank in player_o2_tanks])
    health_text = font.render(
        f'HEALTH: {math.ceil(player_character.health)}/{player_character.maxHealth}',
        fgcolor=(255, 255, 255))
    oxygen_text = font.render(
        f'O2: {oxygen_capacity_m3}/{math.ceil(oxygen_volume_m3)}',
        fgcolor=(255, 255, 255))
    screen.blit(health_text[0], [0, 0])
    screen.blit(oxygen_text[0], [0, oxygen_text[1].height])
