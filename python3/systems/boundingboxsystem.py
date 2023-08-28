import pygame
from boundingbox import bounding_boxes, BoundingBox


def overlaps(bounding_box1: BoundingBox, bounding_box2: BoundingBox):
    return not (bounding_box1.x > bounding_box2.x+bounding_box2.width
                or bounding_box1.x+bounding_box1.width < bounding_box2.x
                or bounding_box1.y > bounding_box2.y+bounding_box2.height
                or bounding_box1.y+bounding_box1.height < bounding_box2.y)


def render(screen, x_scale_ratio, y_scale_ratio):
    boxes = []
    for bb in bounding_boxes.values():
        box_surface = pygame.surface.Surface((
                bb.width*x_scale_ratio,
                bb.height*y_scale_ratio
            ),
            pygame.SRCALPHA)
        box_surface.fill((bb.red, bb.green, bb.blue))
        box_surface = pygame.transform.rotate(box_surface, float(bb.rotation_degrees))
        boxes.append((box_surface,
                     (bb.x*x_scale_ratio, bb.y*y_scale_ratio)))
    screen.blits(boxes)
