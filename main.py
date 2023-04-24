import pygame
import random
import math

pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
GRAVITY = 0.0981
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
pygame.display.set_caption("My Physics Engine 1.0")
screen.fill((0, 0, 0))


class Particle:
    def __init__(self, particle_x, particle_y, particle_radius):
        self.particle_speed = 0
        self.particle_x = particle_x
        self.particle_y = particle_y
        self.particle_y_old = particle_y
        self.particle_radius = particle_radius
        self.color = random.choice(colors)
        pygame.draw.circle(screen, self.color, (self.particle_x, self.particle_y), self.particle_radius)

    def collision(self):
        dist_right = SCREEN_WIDTH - self.particle_x
        dist_left = self.particle_x
        dist_bottom = SCREEN_HEIGHT - self.particle_y

        if dist_bottom < self.particle_radius:
            self.particle_y = SCREEN_HEIGHT - self.particle_radius
        if dist_left < self.particle_radius:
            self.particle_x = self.particle_radius
        if dist_right < self.particle_radius:
            self.particle_x = SCREEN_WIDTH - self.particle_radius

    def activate_gravity(self, dt):
        disp_y = self.particle_y - self.particle_y_old
        self.particle_y += disp_y + GRAVITY * dt * dt


    def render(self):
        pygame.draw.circle(screen, self.color, (self.particle_x, self.particle_y), self.particle_radius)


    # def updateDeltaT(self, deltaT):
    #     self.activate_gravity(deltaT=deltaT)
    #     pygame.draw.circle(screen, self.color, (self.particle_x, self.particle_y), self.particle_radius)


running = True
clock = pygame.time.Clock()
particles = []

try:
    while running:
        dt = clock.tick(FPS) / 60

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    pos = pygame.mouse.get_pos()
                    particles.append(Particle(pos[0], pos[1], 20))

        screen.fill((0, 0, 0))

        for particle in particles:
            particle.activate_gravity(dt)
            particle.collision()
            particle.render()

        pygame.display.update()

# only compares collision status with the previous particle and not all the particles


except KeyboardInterrupt:
    pygame.quit()
