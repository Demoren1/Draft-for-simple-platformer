from box import *
from pygame import Color
import pygame

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
LIGHT_BLUE = (57, 242, 182)
TRANSPARANT = (0, 0, 0, 0)

Aqua    = (000,255,255)
Black   = (000,000,000)
Blue    = (000,000,255)
Fuchsia = (255,000,255)
Gray    = (128,128,128)
Green   = (000,128,000)
Lime    = (000,255,000)
Maroon  = (128,000,000)
Navy    = (000,000,128)
Olive   = (128,128,000)
Purple  = (128,000,128)
Red     = (255,000,000)
Silver  = (192,192,192)
Teal    = (000,128,128)
White   = (255,255,255)
Yellow  = (255,255,000)

colors_arr = [Aqua, Black, Blue, Fuchsia, Gray, Green, Lime, Maroon, Navy, Olive, Purple ,Red, Silver, Teal, White, Yellow]
pallete = []

for i in range(16):
    tmp_box = Box(pygame.Rect(40 * (i % 4) + 5, 40 * (i // 4), 40, 40), colors_arr[i], (0, 0), 0)
    pallete.append(tmp_box)