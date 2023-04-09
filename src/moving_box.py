from pygame import Rect
from pygame import Vector2
from pygame.color import Color
import pygame
import box
class Moving_box(box.Box):
    def __init__(self, rect: Rect, color: Color, velocity: Vector2, mass: float):
        super().__init__(rect, color, velocity, mass)
        self.is_static = False
        self.flag_on_earth = False
        self.direction = 0