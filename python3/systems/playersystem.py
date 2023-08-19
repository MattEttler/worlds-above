import math
from config import config
import pygame
from character import Character, characters
from boundingbox import BoundingBox, bounding_boxes
import charactersystem
import entitymanager

def bootstrap(mapSize: int):
    playerCharacter = Character()
    playerBox = BoundingBox()
    playerBox.red = 255
    playerBox.blue = 255
    playerBox.green = 0
    playerBox.outline_size = 0
    playerBox.x = mapSize/2
    playerBox.y = mapSize/2
    return charactersystem.create_character(
            playerCharacter,
            playerBox
            )

base_movement_speed_per_second = config.getint('Player', 'PlayerBaseMovementSpeedPerSecond')
base_movement_speed_per_millisecond = base_movement_speed_per_second / 1000

def update_player(playerId: int, lapsed_milliseconds: int):
    global bounding_boxes
    player_character = bounding_boxes[playerId]
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player_character.x = player_character.x - (base_movement_speed_per_millisecond * lapsed_milliseconds)
    if keys[pygame.K_d]:
        player_character.x = player_character.x + (base_movement_speed_per_millisecond * lapsed_milliseconds)
    if keys[pygame.K_w]:
        player_character.y = player_character.y - (base_movement_speed_per_millisecond * lapsed_milliseconds)
    if keys[pygame.K_s]:
        player_character.y = player_character.y + (base_movement_speed_per_millisecond * lapsed_milliseconds)

'''Render the heads up display for a particular player.'''
def render_hud(player_id, font, screen):
    player_character = characters[player_id]
    text = font.render(
        f'HEALTH: {math.ceil(player_character.health)}/{player_character.maxHealth}',
        fgcolor=(255, 255, 255))
    screen.blit(text[0], [0, 0])
