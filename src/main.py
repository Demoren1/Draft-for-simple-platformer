import pygame
from box import *
from game_funcs import *
import editor
import base
import camera as cam
import objects

WIDTH = 1920
HEIGHT = 1080

camera_w = 1920
camera_h = 1080


def main():
    editing_flag = [False]                #for edit
    edit_result = [False, None, None, None]     #[drawning_flag, start_pos, end_pos,tmp_rect] tmp rect for adding ot massive of all

    pygame.init()
    
    my_COCK = pygame.time.Clock()
    screen1 = pygame.display.set_mode((WIDTH,HEIGHT))
    screen = pygame.Surface((WIDTH, HEIGHT))
    camera = cam.Camera(pygame.Rect(0, 0, camera_w, camera_h))
    while True:
        my_COCK.tick(60)

        my_box = base.handle_moving_box(screen)

        shift = camera.offset_obj_camera(Vector2(my_box.rect.x, my_box.rect.y), base.all_objects)
        camera.offset_camera(Vector2(my_box.rect.x, my_box.rect.y))

        base.draw_objects(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type ==  pygame.MOUSEBUTTONDOWN:           #shoot
                base.handle_shot(event, my_box,camera, 30, objects.moving_objects, objects.all_objects, objects.drawable_objects)
            screen = check_is_need_scale(event, screen, camera)
            edit_result = check_is_need_edit(event, screen, camera, edit_result, editing_flag,
                                             objects.all_objects, objects.drawable_objects, objects.static_scene)

        if edit_result[0]:
            editor.draw_rect(screen, edit_result, shift, camera)

        scaled_screen = pygame.transform.scale(screen, (1920, 1080)) 
        pygame.Surface.blit(screen1, scaled_screen, (0, 0))
        pygame.display.update()
        screen.fill('grey')
        screen1.fill('grey')

def check_is_need_edit(event, screen, camera, edit_result, editing_flag, all_objects, drawable_objects, static_objects):
    
    if event.type == pygame.KEYDOWN and pygame.key.get_pressed()[pygame.K_e]:
        editing_flag[0] = not editing_flag[0]
    if editing_flag[0]:
        edit_result = editor.edit_map(event, edit_result, camera, all_objects, drawable_objects, static_objects) 
                                                                            #todo add adding to massive, and option 
    else:                                                                   #to save in map file
        edit_result = [False, None, None, None]

    return edit_result
def check_is_need_scale(event, screen, camera):
    if event.type == pygame.KEYDOWN:                    #scale
        screen = camera.scale_screen(screen, WIDTH, HEIGHT)
    return screen

main()