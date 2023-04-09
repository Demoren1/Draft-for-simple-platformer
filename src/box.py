from pygame import Rect
from pygame import Vector2
from pygame.color import Color
import pygame

class Box:
    def __init__(self, rect: Rect, color: Color, velocity: Vector2, mass: float):
        self.rect = rect
        self.color = color
        self.velocity = velocity
        self.mass = mass
        self.is_static = True
    def get_image_for_box(self):
        self.image = pygame.Surface((self.rect.width, self.rect.height))
        pygame.draw.rect(self.image, self.color, self.rect)

def draw_box(surface:pygame.Surface, box: Box):
    pygame.draw.rect(surface, box.color, box.rect)
