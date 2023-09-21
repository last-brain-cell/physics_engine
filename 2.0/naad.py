import pygame
import math
import random


pygame.init()
pygame.mixer.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
GRAVITY = 0.098
FPS = 60
colors = [
    (255, 0, 0),  # red
    (0, 255, 0),  # green
    (0, 0, 255),  # blue
    (255, 255, 0),  # yellow
    (255, 0, 255),  # magenta
    (0, 255, 255),  # cyan
    (255, 128, 0),  # orange
    (128, 0, 255),  # purple
    (255, 192, 203),  # pink
    (128, 128, 128),  # gray
    (255, 255, 255),  # white
]

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My Physics Engine 2.0")
screen.fill((0, 0, 0))

class Particle:

    def __init__(self):

    def apply_gravity(self):
        self.velocity[1] += GRAVITY