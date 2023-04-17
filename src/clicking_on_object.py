import pygame
import typing
from pygame import Vector2
import camera as cam
from box import *
from colors import *
import objects
import editor

class Clicker:
    def __init__(self):
        self.clicked_flag = False
        self.pos = None
        self.clicked_obj = None

    def get_clicked_obj(self, event, objects_to_check):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.pos = pygame.mouse.get_pos()
            self.get_obj(objects_to_check)

    def get_obj(self, objects_to_check: Box):
        for box in objects_to_check:
            rect = box.rect
            if rect.x < self.pos[0] and self.pos[0] < (rect.x + rect.width) and \
               rect.y < self.pos[1] and self.pos[1] < (rect.y + rect.height):
                self.clicked_obj = box
                return box
        self.clicked_obj = None
        self.clicked_flag = False
        
