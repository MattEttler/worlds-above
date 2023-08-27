from config import config
import numpy as N
import pygame
from light import lights
from boundingbox import bounding_boxes

diffuse_distance = config.getint('Lighting', 'DiffusionDistance')
intensity_loss_per_ms = config.getint(
        'Lighting', 'IntensityLossPerSecond'
        ) / 1000

filter_surf = pygame.surfarray.make_surface(
        N.zeros((diffuse_distance, diffuse_distance, 3))
        )
clean_whole_filter = None

width = None
height = None
x_scale_ratio = None
y_scale_ratio = None
glow_width = None
glow_height = None
'''Create the full-brightness template used for drawing each light.'''


def initialize_lighting_surface(
        mapSize: int,
        x1_scale_ratio: int,
        y1_scale_ratio: int
        ):
    global filter_surf
    global glow_array
    global clean_whole_filter
    global lighting_surface
    global width, height, x_scale_ratio, y_scale_ratio, glow_width, glow_height

    width = int(mapSize*x1_scale_ratio)
    height = int(mapSize*y1_scale_ratio)
    x_scale_ratio = x1_scale_ratio
    y_scale_ratio = y1_scale_ratio

    diffuse_x_scaled = int(diffuse_distance*x_scale_ratio)
    diffuse_y_scaled = int(diffuse_distance*y_scale_ratio)
    diffuse_img_size = int(N.sqrt((diffuse_x_scaled/2)**2
                                  + (diffuse_y_scaled/2)**2))
    arr = N.zeros((int(diffuse_img_size), int(diffuse_img_size), 3))
    for i in range(diffuse_img_size):
        for j in range(diffuse_img_size):
            distance = N.sqrt(
                    (i-(diffuse_img_size//2))**2
                    + (j-(diffuse_img_size//2))**2
                    )
            intensity = int(distance
                            / (N.sqrt((diffuse_img_size//2)**2
                                      + (diffuse_img_size//2)**2)) * 255
                            )
            arr[i, j] = (intensity, intensity, intensity)
    clean_whole_filter = pygame.surface.Surface(
            (mapSize*x_scale_ratio, mapSize*y_scale_ratio)
            ).convert_alpha()
    pygame.Surface.fill(clean_whole_filter, pygame.Color('white'))
    filter_surf = pygame.surfarray.make_surface(arr).convert_alpha()


def update_lights(lapsed_milliseconds: int):
    for entity in lights.keys():
        if lights[entity].intensity < 255:
            lights[entity].intensity = min(
                    255,
                    lights[entity].intensity
                    + intensity_loss_per_ms
                    * lapsed_milliseconds
                    )


'''draw each light to the screen.'''


# need to optimize! Only 20 lights and the poor thing crawls to it's knees.
def render_lights(screen, x_scale_ratio: int, y_scale_ratio: int):
    whole_filter = clean_whole_filter.copy()
    blits_sequence = []
    for entity in lights.keys():
        light_box = bounding_boxes[entity]
        glow_top = int(
                (light_box.x*x_scale_ratio)
                - (filter_surf.get_width()/2))
        glow_left = int(
                (light_box.y*y_scale_ratio)
                - (filter_surf.get_height()/2)
                )
        intensity_filter = filter_surf.copy()
        blits_sequence.append((
            intensity_filter, (
                glow_top,
                glow_left
                ),
            None,
            pygame.BLEND_RGBA_MULT
            ))
        pygame.Surface.fill(
                intensity_filter,
                    (
                    lights[entity].intensity,
                    lights[entity].intensity,
                    lights[entity].intensity
                    ),
                special_flags=pygame.BLEND_RGB_ADD
                )
    whole_filter.blits(tuple(blits_sequence))
    screen.blit(whole_filter, (0, 0), special_flags=pygame.BLEND_RGBA_SUB)
