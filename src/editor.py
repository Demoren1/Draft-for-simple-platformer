import pygame
import typing
from pygame import Vector2
import camera as cam
from box import *
from colors import *
import objects

class Editor:
    def __init__(self, drawning, start_pos, end_pos, arr_of_tmp_boxes):
        self.drawning = drawning
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.arr_of_tmp_boxes = arr_of_tmp_boxes
        self.editing_flag = False
        self.tmp_box = None
        self.current_color = 0

    def edit_map(self, event: pygame.event, camera: cam.Camera):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.current_color = 0
            self.drawning = True
            self.start_pos = list(pygame.mouse.get_pos())
            self.start_pos = check_for_scale(self.start_pos, camera)

        if event.type == pygame.MOUSEBUTTONUP:
            self.drawning = False
            self.arr_of_tmp_boxes.append(self.tmp_box)

        if self.drawning and pygame.MOUSEMOTION:
            self.end_pos = list(pygame.mouse.get_pos())
            self.end_pos = check_for_scale(self.end_pos, camera)

    def draw_editable_rect(self, screen, shift):

        if self.start_pos == None or self.end_pos == None:
            return None
        
        correction_x = 0
        correction_y = 0
        if self.end_pos[0] - self.start_pos[0] < 0:
            correction_x = self.start_pos[0] - self.end_pos[0]
        
        if self.end_pos[1] - self.start_pos[1] < 0:
            correction_y = self.start_pos[1] - self.end_pos[1]

        box = Box(pygame.Rect((self.start_pos[0] - correction_x, self.start_pos[1] - correction_y),
                            (self.end_pos[0] - self.start_pos[0] + 2 * correction_x, self.end_pos[1] - self.start_pos[1] + 2 * correction_y)),
                            BLUE, Vector2(0, 0), 0)
        
        for i in range(len(shift)): self.start_pos[i] += shift[i]

        pygame.draw.rect(screen, 'blue', box.rect)

        self.tmp_box = box
    
    def handle_edit_result(self, screen: pygame.Surface, shift):
        if self.drawning:
            self.draw_editable_rect(screen, shift)

        if self.arr_of_tmp_boxes != []:
            for box in self.arr_of_tmp_boxes:
                draw_box(screen, box)
                handle_rect_with_shift(box.rect, shift)

    def del_box_from_arr(self):
        self.arr_of_tmp_boxes.pop()

    def change_color(self):
        box = self.arr_of_tmp_boxes[-1]
        box.color = colors_arr[self.current_color % len(colors_arr)]
        self.current_color += 1

def check_for_scale(pos: list, camera: cam.Camera):
    if camera.scaled < 0:
        for i in range(len(pos)):
            pos[i] *= 2 ** (abs(camera.scaled))
    if camera.scaled > 0:
        for i in range(len(pos)):
            pos[i] /= 2 ** (abs(camera.scaled))
    
    return pos


def handle_rect_with_shift(rect: pygame.Rect, shift: typing.Iterable):
    rect.x += shift[0]
    rect.y += shift[1]

def add_boxes_to_arrays(adding_boxes, static_scene, all_objects, drawable_objects):
    for box in adding_boxes:
        static_scene.append(box)
        all_objects.append(box)
        drawable_objects.append(box)

def check_is_need_edit(event, camera, editor: Editor):
    
    if event.type == pygame.KEYDOWN and pygame.key.get_pressed()[pygame.K_e]:
        editor.editing_flag = not editor.editing_flag
    if editor.editing_flag:
        editor.edit_map(event, camera)
    else:                                                                   
        editor.drawning = False
        editor.start_pos = None
        editor.end_pos = None
        editor.arr_of_tmp_boxes = []
        editor.num_of_tmp_boxes = 0

    if event.type == pygame.KEYDOWN and pygame.key.get_pressed()[pygame.K_p] and editor.arr_of_tmp_boxes != []:
        add_boxes_to_arrays(editor.arr_of_tmp_boxes, objects.static_scene, objects.all_objects, objects.drawable_objects)
        editor.arr_of_tmp_boxes = []
        editor.num_of_tmp_boxes = 0

    if event.type == pygame.KEYDOWN and pygame.key.get_pressed()[pygame.K_o] and editor.arr_of_tmp_boxes != []:
        editor.del_box_from_arr()

    if event.type == pygame.KEYDOWN and pygame.key.get_pressed()[pygame.K_i] and editor.arr_of_tmp_boxes != []:
        editor.change_color()