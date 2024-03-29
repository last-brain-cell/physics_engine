import pygame
import math
import random

pygame.init()

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
    def __init__(self, radius, mass, x, y, initial_x_velocity=0, initial_y_velocity=0):
        self.mass = mass
        self.velocity = [initial_x_velocity, initial_y_velocity]
        self.radius = radius
        self.x = x
        self.y = y
        self.color = random.choice(colors)
        self.density = 1.21
        self.restitution = 0.99

    def apply_gravity(self):
        self.velocity[1] += GRAVITY

    def apply_force(self, force: list, dt=1 / 60):
        acceleration = [0, 0]
        acceleration[0] = force[0] / self.mass
        acceleration[1] = force[1] / self.mass
        self.velocity[0] += acceleration[0] * dt
        self.velocity[1] += acceleration[1] * dt

    def apply_friction_x(self, friction: float = 0.99):
        self.velocity[0] *= friction

    def update_position(self):
        self.x += self.velocity[0]
        self.y += self.velocity[1]

    def render(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def stay_in_window(self):
        dist_right = SCREEN_WIDTH - self.x
        dist_left = self.x
        dist_bottom = SCREEN_HEIGHT - self.y
        dist_top = self.y

        if dist_bottom < self.radius:
            self.y = SCREEN_HEIGHT - self.radius
        if dist_left < self.radius:
            self.x = self.radius
        if dist_right < self.radius:
            self.x = SCREEN_WIDTH - self.radius
        if dist_top < self.radius:
            self.y = self.radius

    def collision_check(self, particles: list, i):
        for j in range(i, len(particles)):
            if -particles[i].radius < particles[i].x - particles[j].x < particles[i].radius:
                particles[i].x += particles[i].x - particles[j].x
            if -particles[i].y < particles[i].y - particles[j].y < particles[i].radius:
                particles[i].y += particles[i].y - particles[j].y


running = True
clock = pygame.time.Clock()
particles = []

try:
    count = 0
    while running:
        count += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    pos = pygame.mouse.get_pos()
                    particles.append(Particle(20, 50, pos[0], pos[1], initial_x_velocity=random.randint(0, 0)))
                    print(len(particles))

        screen.fill((0, 0, 0))

        for i in range(len(particles)):
            particles[i].apply_gravity()
            particles[i].stay_in_window()
            particles[i].apply_friction_x(0.99)
            particles[i].apply_force(force=[0, 20])
            particles[i].update_position()
            particles[i].stay_in_window()
            particles[i].render(screen)

        pygame.display.update()

except KeyboardInterrupt:
    pygame.quit()

# for j in range(i, len(particles)):
#     if -particles[i].radius < particles[i].x - particles[j].x < particles[i].radius:
#         particles[i].x += particles[i].x - particles[j].x
#     if -particles[i].y < particles[i].y - particles[j].y < particles[i].radius:
#         particles[i].y += particles[i].y - particles[j].y
#
