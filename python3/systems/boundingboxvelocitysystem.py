import math
from boundingbox import bounding_boxes
from velocity import velocities


'''Apply Velocities to Bounding_Boxes'''


def apply_velocities_to_bounding_boxes(lapsed_milliseconds: int):
    for entity in velocities.keys():
        if bounding_boxes.get(entity, None) is not None:
            bounding_boxes[entity].rotation_degrees = math.degrees(math.atan2(
                    max(-1, min(velocities[entity].x_delta_per_millisecond, 1)),
                    max(-1, min(velocities[entity].y_delta_per_millisecond, 1))
                    ))
            bounding_boxes[entity].x \
                += velocities[entity].x_delta_per_millisecond \
                * lapsed_milliseconds
            bounding_boxes[entity].y \
                += velocities[entity].y_delta_per_millisecond \
                * lapsed_milliseconds
