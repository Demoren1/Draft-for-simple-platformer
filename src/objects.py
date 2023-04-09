import pygame
from box import *
from game_funcs import *
from moving_box import *
from colors import *
from moving_box import *

WIDTH = 1920
HEIGHT = 1080

a = 0.5

my_box = Moving_box(Rect(3000, 700, 50, 150), BLUE, Vector2(0, 0), 10)
my_box.is_static = False
my_box.flag_on_earth = False
my_box.direction = 0
    
random_box = Box(Rect(250, 300, 400, 400), RED, Vector2(0, 0), 10)
random_box2 = Box(Rect(1050, 300, 400, 400), LIGHT_BLUE, Vector2(0, 0), 10)

earth = Box(Rect(0, HEIGHT - 100, WIDTH * 2, 150), GREEN, Vector2(0, 0), 999)
left_bonce = Box(Rect(0, 0, 10, HEIGHT), GREEN, Vector2(0, 0), 999)
right_bounce = Box(Rect(2*WIDTH - 10, 0, 10, HEIGHT), GREEN, Vector2(0, 0), 999)
up_bounce = Box(Rect(0, 0, 2*WIDTH, 10), GREEN, Vector2(0, 0), 999)

all_objects = [earth, left_bonce, right_bounce, up_bounce, random_box, random_box2, my_box]
static_scene = [earth, left_bonce, right_bounce, up_bounce, random_box, random_box2]
drawable_objects = [my_box, earth, left_bonce, right_bounce, up_bounce, random_box, random_box2]
moving_objects = [my_box]