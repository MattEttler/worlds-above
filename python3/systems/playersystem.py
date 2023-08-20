import math
from config import config
import pygame
from character import Character, characters
from boundingbox import BoundingBox, bounding_boxes
from container import Container, containers
import charactersystem
import entitymanager
import gamestatemanager

def bootstrap(mapSize: int):
    playerCharacter = Character()
    playerBox = BoundingBox()
    playerBox.red = 255
    playerBox.blue = 255
    playerBox.green = 0
    playerBox.outline_size = 0
    playerBox.x = mapSize/2
    playerBox.y = mapSize/2
    playerInventory = Container([])
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
    if keys[pygame.K_a]:
        player_box.x = player_box.x - (base_movement_speed_per_millisecond * lapsed_milliseconds)
    if keys[pygame.K_d]:
        player_box.x = player_box.x + (base_movement_speed_per_millisecond * lapsed_milliseconds)
    if keys[pygame.K_w]:
        player_box.y = player_box.y - (base_movement_speed_per_millisecond * lapsed_milliseconds)
    if keys[pygame.K_s]:
        player_box.y = player_box.y + (base_movement_speed_per_millisecond * lapsed_milliseconds)

    if player_character.health <= 0:
        gamestatemanager.game_state = gamestatemanager.GameState.OVER


'''Render the heads up display for a particular player.'''


def render_hud(player_id, font, screen):
    player_character = characters[player_id]
    text = font.render(
        f'HEALTH: {math.ceil(player_character.health)}/{player_character.maxHealth}',
        fgcolor=(255, 255, 255))
    screen.blit(text[0], [0, 0])
