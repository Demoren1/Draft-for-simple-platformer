import pygame
from box import *
from game_funcs import *
from moving_box import *
from colors import *
from objects import *
import editor

def handle_moving_box():
    my_box.velocity.y += a

    moving_box(my_box)
    for moving_obj in moving_objects:
        handle_moving_obj(moving_obj)
        if moving_obj is my_box:
            my_box.flag_on_earth = False
        for object in static_scene:
            if is_overlap(moving_obj, object):
                push_vector = get_correction_vector(moving_obj, object)
                if push_vector.x and push_vector.x * moving_obj.velocity.x < 0:
                    moving_obj.velocity.x = 0
                if push_vector.y and push_vector.y * moving_obj.velocity.y < 0:
                    moving_obj.velocity.y = 0

                moving_obj.rect.x += push_vector.x
                moving_obj.rect.y += push_vector.y
                if moving_obj is my_box:
                    my_box.flag_on_earth = push_vector.y < 0

    return my_box

def draw_objects(screen):
    for object in drawable_objects:
        
        draw_box(screen, object)
