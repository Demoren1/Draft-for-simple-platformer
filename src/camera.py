from pygame import Rect, Vector2
import pygame
import box
class Camera:
    def __init__(self, camera:Rect):
        self.camera = camera
        self.scaled = 0
        self.delta_scaled = 0

    def offset_obj_camera(self, cord_main_obj: Vector2, all_objects):
        delta_x = self.camera.x + self.camera.width / 2 - cord_main_obj.x
        delta_y = self.camera.y + self.camera.height / 2 - cord_main_obj.y   

        for i in all_objects:
            i.rect.x += delta_x
            i.rect.y += delta_y
        return delta_x, delta_y

    def offset_camera(self, cord_main_obj: Vector2):
        self.camera.x, self.camera.y = cord_main_obj.x - self.camera.width // 2, cord_main_obj.y - self.camera.height // 2  
    
    def scale_screen(self, screen: pygame.Surface, width, height):
        prev_scale = self.scaled
        if pygame.key.get_pressed()[pygame.K_EQUALS] and self.scaled < 4:
            self.camera.x -= screen.get_width() / 4
            self.camera.y -= screen.get_height() / 4
            screen = pygame.Surface((screen.get_width() / 2, screen.get_height() / 2))

            self.scaled += 1

        if pygame.key.get_pressed()[pygame.K_MINUS] and self.scaled > -4:
            self.camera.x += screen.get_width() / 2
            self.camera.y += screen.get_height() / 2
            screen = pygame.Surface((screen.get_width() * 2, screen.get_height() * 2))

            self.scaled -= 1
        self.delta_scaled = prev_scale - self.scaled
        return screen
            