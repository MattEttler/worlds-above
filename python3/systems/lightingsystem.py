import math
from config import config
import numpy as N
import pygame
from light import Light, lights
from boundingbox import bounding_boxes

diffuse_distance = config.getint('Lighting', 'DiffusionDistance')

filter_surf = pygame.surfarray.make_surface(N.zeros((diffuse_distance, diffuse_distance, 3)))

'''Draw light sources.'''



def initialize_lighting_surface(mapSize: int, x_scale_ratio: float, y_scale_ratio: float):
    global filter_surf
    diffuse_scaled = int(diffuse_distance*x_scale_ratio)
    arr = N.zeros((diffuse_scaled, diffuse_scaled, 3))
    for i in range(diffuse_scaled):
        for j in range(diffuse_scaled):
            distance = N.sqrt((i-(diffuse_scaled//2))**2 + (j-(diffuse_scaled//2))**2)
            intensity = int(distance / (N.sqrt((diffuse_scaled//2)**2+(diffuse_scaled//2)**2)) * 255)
            arr[i, j] = (intensity, intensity, intensity)
    filter_surf = pygame.surfarray.make_surface(arr)


def render_lights(screen, x_scale_ratio: int, y_scale_ratio: int):
    blits_sequence = tuple([(
        # sometimes the following line generates a keyError because we attemptt to find a bounding_box that does not exist???
        filter_surf, (int((bounding_boxes[entity].x*x_scale_ratio)-(filter_surf.get_width()/2)), int((bounding_boxes[entity].y*y_scale_ratio)-(filter_surf.get_height()/2))), None, pygame.BLEND_RGBA_MULT) for entity in lights.keys()])
    whole_filter = pygame.surface.Surface((screen.get_width(), screen.get_height()))
    pygame.Surface.fill(whole_filter, pygame.Color('white'))
    whole_filter.blits((blits_sequence))
    screen.blit(whole_filter, (0, 0), special_flags=pygame.BLEND_RGBA_SUB)
