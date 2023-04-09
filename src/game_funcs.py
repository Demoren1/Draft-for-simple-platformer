import pygame
import box
from pygame import Vector2
from moving_box import *
from colors import *
import camera as cam

def moving_box(sq_box: box.Box):
    if sq_box.is_static:
        return None
    
    a = 20
    jump_a = -250

    if pygame.key.get_pressed()[pygame.K_w] and sq_box.flag_on_earth:
        sq_box.velocity.y = -20
    if pygame.key.get_pressed()[pygame.K_s]:
        # sq_box.velocity.y += a
        sq_box.rect.y += 1
    if pygame.key.get_pressed()[pygame.K_a]:
        # sq_box.velocity.x -= a
        sq_box.rect.x -= a
    if pygame.key.get_pressed()[pygame.K_d]:
        # sq_box.velocity.x += a
        sq_box.rect.x += a
    
    sq_box.rect.x += sq_box.velocity.x
    sq_box.rect.y += sq_box.velocity.y

def handle_moving_obj(moving_obj: box.Box):
    moving_obj.rect.x += moving_obj.velocity.x
    moving_obj.rect.y += moving_obj.velocity.y


def is_overlap(box1:box.Box, box2:box.Box) -> int:
    rect1 = box1.rect
    rect2 = box2.rect
    return ((rect1.x + rect1.width) > rect2.x and (rect2.x + rect2.width) > rect1.x and 
            (rect1.y + rect1.height) > rect2.y and (rect2.y + rect2.height) > rect1.y)

def get_correction_vector(box1: box.Box, box2 : box.Box):
    rect1 = box1.rect
    rect2 = box2.rect

    y1_top = rect1.y
    y2_top = rect2.y
    y1_bottom = y1_top + rect1.height
    y2_bottom = y2_top + rect2.height

    x1_left = rect1.x
    x2_left = rect2.x
    x1_right = x1_left + rect1.width
    x2_right = x2_left + rect2.width

    if abs(x1_right - x2_left) < abs(x1_left - x2_right):
        push_x = x2_left - x1_right
    else:
        push_x = x2_right - x1_left

    if abs(y1_bottom - y2_top) < abs(y1_top - y2_bottom):
        push_y = y2_top - y1_bottom
    else:
        push_y = y2_bottom - y1_top

    return Vector2(push_x, 0) if abs(push_x) <= abs(push_y) else Vector2(0, push_y)

def handle_shot(event:pygame.event, my_box:box.Box, camera: cam.Camera, shot_speed:float, moving_objects, all_objects, drawable_objects):
    if event.button == 1:
        bullet = Moving_box(Rect(my_box.rect.x, my_box.rect.y, 10, 20), BLACK, Vector2(0, 0), 1)
        bullet.is_static = False

        mouse_pos = list(pygame.mouse.get_pos())
        mouse_pos = check_for_scale(mouse_pos, camera)

        mouse_pos[0], mouse_pos[1] = mouse_pos[0] - my_box.rect.x, mouse_pos[1] - my_box.rect.y

        if mouse_pos[0] == 0:
            mouse_pos[0] = 1
        if mouse_pos[1] == 0:
            mouse_pos[1] = 1

        proportion = abs(mouse_pos[0]) / (abs(mouse_pos[0]) + abs(mouse_pos[1]))
        bullet.velocity.x = shot_speed * proportion * abs(mouse_pos[0]) / mouse_pos[0]
        bullet.velocity.y = shot_speed * (1 - proportion) * abs(mouse_pos[1]) / mouse_pos[1]

        moving_objects.append(bullet)
        drawable_objects.append(bullet)
        all_objects.append(bullet)

def check_for_scale(pos: list, camera: cam.Camera):
    if camera.scaled < 0:
        for i in range(len(pos)):
            pos[i] *= 2 ** (abs(camera.scaled))
    if camera.scaled >0:
        for i in range(len(pos)):
            pos[i] /= 2 ** (abs(camera.scaled))
    
    return pos








