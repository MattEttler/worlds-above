'''Entry Script. This is the main scrupt which is intended to be run to play
worlds above'''
# Inlude our component and system folders into the module path.
import os
import sys
import pygame
from config import config

import entitymanager
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
clock = pygame.time.Clock()
RUNNING = True
DELTA_TIME_MILLISECONDS = 0

# Import our game-components.
import boundingbox

# Import our game-systems.
import boundingboxsystem
import charactersystem


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

# Populate characters on the map
charactersystem.bootstrap_characters(mapSize)


#####################
# MAIN PROGRAM LOOP #
#####################

while RUNNING:
    # Check for program termination
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            RUNNING = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        RUNNING = False

    # Logical Updates
    charactersystem.update_characters(fortress, DELTA_TIME_MILLISECONDS)

    # Graphical Updates
    screen.fill((10, 10, 80))
    boundingboxsystem.render(screen, screenWidth/mapSize, screenHeight/mapSize)
    pygame.display.flip()

    DELTA_TIME_MILLISECONDS = clock.tick(60)
pygame.quit()
