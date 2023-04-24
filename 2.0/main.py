import os

import pygame
import math
import random

pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
GRAVITY = 9.8
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
    def __init__(self, radius, mass, x, y):
        self.mass = mass
        self.velocity = [0, 0]
        self.radius = radius
        self.x = x
        self.y = y
        self.color = random.choice(colors)

    def apply_force(self, force: list):
        acceleration = [0, 0]
        acceleration = [force[0] / self.mass, force[1] / self.mass]
        self.velocity[0] += acceleration[0]
        self.velocity[1] += acceleration[1]

    def update_position(self):
        self.x += self.velocity[0]
        self.y += self.velocity[1]

    def render(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def collision(self):
        dist_right = SCREEN_WIDTH - self.x
        dist_left = self.x
        dist_bottom = SCREEN_HEIGHT - self.y

        if dist_bottom < self.radius:
            self.y = SCREEN_HEIGHT - self.radius
        if dist_left < self.radius:
            self.x = self.radius
        if dist_right < self.radius:
            self.x = SCREEN_WIDTH - self.radius

        pass

running = True
clock = pygame.time.Clock()
particles = []

try:
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    pos = pygame.mouse.get_pos()
                    particles.append(Particle(20, 50, pos[0], pos[1]))

        screen.fill((0, 0, 0))

        for particle in particles:
            particle.apply_force([2, GRAVITY])
            particle.update_position()
            particle.collision()
            particle.render(screen)

        # Console:
        print(f"Particles: {len(particles)}")

        pygame.display.flip()

except KeyboardInterrupt:
    pygame.quit()
