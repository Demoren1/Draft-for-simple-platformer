import pygame
from pygame import Vector2
import camera as cam
from box import *
from colors import *

def edit_map(event: pygame.event, prev_result, camera: cam.Camera, all_objects, drawable_objects, static_objects):
    drawning = prev_result[0]
    start_pos = prev_result[1]
    end_pos = prev_result[2]
    tmp_rect = prev_result[3]
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        drawning = True
        start_pos = list(pygame.mouse.get_pos())
        start_pos = check_for_scale(start_pos, camera)

    if event.type == pygame.MOUSEBUTTONUP:
        drawning = False
        all_objects.append(tmp_rect)
        drawable_objects.append(tmp_rect)
        static_objects.append(tmp_rect)


    if drawning and pygame.MOUSEMOTION:
        end_pos = list(pygame.mouse.get_pos())
        end_pos = check_for_scale(end_pos, camera)

    return [drawning, start_pos, end_pos, tmp_rect]

def draw_rect(screen, edit_result, shift, camera: cam.Camera ):
    start_pos, end_pos = edit_result[1], edit_result[2]

    if start_pos == None or end_pos == None:
        return None
    
    correction_x = 0
    correction_y = 0
    if end_pos[0] - start_pos[0] < 0:
        correction_x = start_pos[0] - end_pos[0]
    
    if end_pos[1] - start_pos[1] < 0:
        correction_y = start_pos[1] - end_pos[1]

    rect = Box(pygame.Rect((start_pos[0] - correction_x, start_pos[1] - correction_y),
                          (end_pos[0] - start_pos[0] + 2 * correction_x, end_pos[1] - start_pos[1] + 2 * correction_y)),
                           BLUE, Vector2(0, 0), 0)
    
    for i in range(len(shift)): start_pos[i] += shift[i]

    pygame.draw.rect(screen, 'blue', rect)

    edit_result[3] = rect
    return rect

def check_for_scale(pos: list, camera: cam.Camera):
    if camera.scaled < 0:
        for i in range(len(pos)):
            pos[i] *= 2 ** (abs(camera.scaled))
    if camera.scaled > 0:
        for i in range(len(pos)):
            pos[i] /= 2 ** (abs(camera.scaled))
    
    return pos