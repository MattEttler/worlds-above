# Inlude our component and system folders into the module path.
import os
import sys

app_dir = os.path.dirname( __file__ )
systems_dir = os.path.join( app_dir, 'systems')
components_dir = os.path.join( app_dir, 'components')
sys.path.append( systems_dir )
sys.path.append( components_dir )

# Import our game-components.
import boundingbox

# Import our game-systems.
import boundingboxsystem

# Include our graphics library and configurations
import pygame
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

screenWidth = config.getint('Graphics', 'ScreenWidth')
screenHeight = config.getint('Graphics', 'ScreenHeight')
mapSize = config.getint('Graphics', 'MapSize')

pygame.init()
screen = pygame.display.set_mode((screenWidth, screenHeight))
clock = pygame.time.Clock()
running = True

# Create a Fortress
fortressWidth = config.getint('Fortress', 'Width')
fortressHeight = config.getint('Fortress', 'Height')
fortressRed = config.getint('Fortress', 'Red')
fortressGreen = config.getint('Fortress', 'Green')
fortressBlue = config.getint('Fortress', 'Blue')
fortress = boundingbox.BoundingBox((mapSize-fortressWidth)/2, (mapSize-fortressHeight)/2, fortressWidth, fortressHeight, 0, fortressRed, fortressGreen, fortressBlue)

boundingbox.bounding_boxes[0] = fortress

while running:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            running = False

    screen.fill((10,10,80))

    boundingboxsystem.render(screen, screenWidth/mapSize, screenHeight/mapSize)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
