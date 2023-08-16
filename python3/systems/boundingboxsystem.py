import pygame
import boundingbox

def render(screen, x_scale_ratio, y_scale_ratio):
    for bb in boundingbox.bounding_boxes.values():
        pygame.draw.rect(screen, (bb.red, bb.green, bb.blue), pygame.Rect(bb.x*x_scale_ratio, bb.y*y_scale_ratio, bb.width*x_scale_ratio, bb.height*y_scale_ratio), bb.outline_size)
