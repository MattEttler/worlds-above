import pygame
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

screenWidth = config.getint('Graphics', 'ScreenWidth')
screenHeight = config.getint('Graphics', 'ScreenHeight')

pygame.init()
screen = pygame.display.set_mode((screenWidth, screenHeight))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            running = False

    screen.fill("blue")

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
