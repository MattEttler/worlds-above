'''Entry Script. This is the main script which is intended to be run to play
worlds above'''

# Inlude our component and system folders into the module path.
import os
import sys
import time
import pygame
from config import config

import entitymanager
from gamestatemanager import GameState
import gamestatemanager
app_dir = os.path.dirname(__file__)
systems_dir = os.path.join(app_dir, 'systems')
components_dir = os.path.join(app_dir, 'components')
sys.path.append(systems_dir)
sys.path.append(components_dir)

screenWidth = config.getint('Graphics', 'ScreenWidth')
screenHeight = config.getint('Graphics', 'ScreenHeight')
mapSize = config.getint('Graphics', 'MapSize')

pygame.init()
screen = pygame.display.set_mode((screenWidth, screenHeight))
hud_font = pygame.freetype.Font(None, 20)
clock = pygame.time.Clock()
RUNNING = True
DELTA_TIME_MILLISECONDS = 0

# Import our game-components.
import boundingbox

# Import our game-systems.
import boundingboxsystem
import charactersystem
import playersystem
import oxygentankspawnsystem
import charactercontainablecollisionsystem
import lightingsystem
import lightspawnsystem
import sharkspawnsystem
import characterlightcollisionsystem
import boundingboxvelocitysystem

####################################
# Initialize the state of the game #
####################################

# Create a Fortress
fortressWidth = config.getint('Fortress', 'Width')
fortressHeight = config.getint('Fortress', 'Height')
fortressRed = config.getint('Fortress', 'Red')
fortressGreen = config.getint('Fortress', 'Green')
fortressBlue = config.getint('Fortress', 'Blue')
fortress = boundingbox.BoundingBox(
        (mapSize-fortressWidth)/2, (mapSize-fortressHeight)/2,
        fortressWidth, fortressHeight,
        0,
        fortressRed, fortressGreen, fortressBlue)
boundingbox.bounding_boxes[entitymanager.create_entity()] = fortress

lightingsystem.initialize_lighting_surface(mapSize, screenWidth/mapSize, screenHeight/mapSize)

#####################
# MAIN PROGRAM LOOP #
#####################
while gamestatemanager.game_state is not GameState.QUIT:
    # Check for program termination
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gamestatemanager.game_state = GameState.QUIT

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        gamestatemanager.game_state = GameState.QUIT

    # Bootstrap the game
    if gamestatemanager.game_state == GameState.BOOTING:
        oxygentankspawnsystem.bootstrap_oxygen_tanks(mapSize)
        charactersystem.bootstrap_characters(mapSize)
        playerId = playersystem.bootstrap(mapSize)
        lightspawnsystem.bootstrap_lights(mapSize)
        gamestatemanager.game_state = GameState.RUNNING
        screen.fill((10, 10, 80))
        welcome_text = hud_font.render(
                    "WELCOME TO WORLDS ABOVE",
                    fgcolor=(255, 255, 255)
                )
        screen.blit(welcome_text[0], [(screenWidth-welcome_text[1].width)/2, screenHeight/2])
        pygame.display.flip()
        time.sleep(1)
    elif gamestatemanager.game_state == GameState.OVER:
        if keys[pygame.K_RETURN]:
            gamestatemanager.game_state = GameState.BOOTING
        over_text = hud_font.render(
                    "AQUANAUT DIED. Hit <Enter> to restart.",
                    fgcolor=(255, 255, 255)
                )
        screen.blit(over_text[0], [(screenWidth-over_text[1].width)/2, screenHeight/2])
        pygame.display.flip()
    # Logical Updates
    elif gamestatemanager.game_state == GameState.RUNNING:
        charactersystem.update_characters(fortress, DELTA_TIME_MILLISECONDS)
        playersystem.update_player(playerId, DELTA_TIME_MILLISECONDS)
        charactercontainablecollisionsystem \
            .update_character_containable_collisions()
        lightingsystem.update_lights(DELTA_TIME_MILLISECONDS)
        characterlightcollisionsystem.update_character_light_collisions()
        boundingboxvelocitysystem.apply_velocities_to_bounding_boxes(DELTA_TIME_MILLISECONDS)
        sharkspawnsystem.despawn_sharks(mapSize)
        sharkspawnsystem.spawn_sharks(mapSize)

        # Graphical Updates
        screen.fill((10, 10, 80))
        boundingboxsystem.render(screen, screenWidth/mapSize, screenHeight/mapSize)
        lightingsystem.render_lights(screen, screenWidth/mapSize, screenHeight/mapSize)
        playersystem.render_hud(playerId, hud_font, screen)
        fps_text = hud_font.render(f"FPS: {int(clock.get_fps())}",
                                   fgcolor=(0, 255, 0))
        screen.blit(fps_text[0], [screenWidth-fps_text[1].width, fps_text[1].height])
        pygame.display.flip()

        DELTA_TIME_MILLISECONDS = clock.tick(60)
pygame.quit()
