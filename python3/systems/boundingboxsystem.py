import pygame
from boundingbox import bounding_boxes, BoundingBox


def overlaps(bounding_box1: BoundingBox, bounding_box2: BoundingBox):
    return not (bounding_box1.x > bounding_box2.x+bounding_box2.width
        or bounding_box1.x+bounding_box1.width < bounding_box2.x
        or bounding_box1.y > bounding_box2.y+bounding_box2.height
        or bounding_box1.y+bounding_box1.height < bounding_box2.y)
 


def render(screen, x_scale_ratio, y_scale_ratio):
    for bb in bounding_boxes.values():
        pygame.draw.rect(screen, (bb.red, bb.green, bb.blue), pygame.Rect(bb.x*x_scale_ratio, bb.y*y_scale_ratio, bb.width*x_scale_ratio, bb.height*y_scale_ratio), bb.outline_size)
