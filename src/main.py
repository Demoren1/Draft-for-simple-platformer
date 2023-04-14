import pygame
from box import *
from game_funcs import *
from editor import *
import base
import camera as cam
import objects

WIDTH = 1920
HEIGHT = 1080

camera_w = 1920
camera_h = 1080

def main():
    # edit_result = [False, None, None, None]     #[drawning, start_pos, end_pos, tmp_rect] tmp rect for adding ot massive of all

    editor = Editor(False, None, None, [])

    pygame.init()
    
    my_COCK = pygame.time.Clock()
    screen1 = pygame.display.set_mode((WIDTH,HEIGHT))
    screen = pygame.Surface((WIDTH, HEIGHT))
    camera = cam.Camera(pygame.Rect(0, 0, camera_w, camera_h))
    while True:
        my_COCK.tick(60)

        my_box = base.handle_moving_box()

        shift = camera.offset_obj_camera(Vector2(my_box.rect.x, my_box.rect.y), base.all_objects)
        camera.offset_camera(Vector2(my_box.rect.x, my_box.rect.y))

        base.draw_objects(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            check_is_need_shoot(event, my_box, camera, editor.editing_flag)
            screen = check_is_need_scale(event, screen, camera)
            check_is_need_edit(event, camera, editor)

        editor.handle_edit_result(screen, shift)

        scaled_screen = pygame.transform.scale(screen, (1920, 1080)) 
        pygame.Surface.blit(screen1, scaled_screen, (0, 0))
        pygame.display.update()
        screen.fill('grey')
        screen1.fill('grey')


def check_is_need_scale(event, screen, camera):
    if event.type == pygame.KEYDOWN:                    #scale
        screen = camera.scale_screen(screen, WIDTH, HEIGHT)
    return screen

def check_is_need_shoot(event, my_box, camera, editing_flag):
    if event.type == pygame.MOUSEBUTTONDOWN and not editing_flag:
        base.handle_shot(event, my_box,camera, 30, objects.moving_objects, objects.all_objects, objects.drawable_objects)


main()