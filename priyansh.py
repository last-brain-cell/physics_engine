import pygame
# import math
import random
import pygame.math as math

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
    def __init__(self, radius, mass, x, y, v_x=0, v_y=0):
        self.mass = mass
        self.radius = radius
        self.position = math.Vector2(x, y)
        self.velocity = math.Vector2(v_x, v_y)
        self.color = random.choice(colors)
        # print(type(self.velocity.y))
        # print(x, self.position.x, self.position.y)

    def apply_gravity(self, dt=1 / 60):
        self.velocity.y = self.velocity.y + GRAVITY * dt

    def apply_friction_x(self, friction: float = 0.97):
        self.velocity.y *= friction * 1 / 60
        self.velocity.x *= friction * 1 / 60

    def update_position(self):
        self.position += self.velocity

    def render(self, screen):
        pygame.draw.circle(screen, self.color, (self.position.x, self.position.y), self.radius)

    def stay_in_window(self):
        dist_top = self.position.y
        dist_right = SCREEN_WIDTH - self.position.x
        dist_left = self.position.x
        dist_bottom = SCREEN_HEIGHT - self.position.y

        if dist_bottom < self.radius:
            self.position.y = SCREEN_HEIGHT - self.radius
            self.velocity = -1 * self.velocity
        if dist_left < self.radius:
            self.position.x = self.radius
            self.velocity = -1 * self.velocity
        if dist_right < self.radius:
            self.position.x = SCREEN_WIDTH - self.radius
            self.velocity = -1 * self.velocity
        if dist_top < self.radius:
            self.position.y = self.radius
            self.velocity = -1 * self.velocity

    def collision_check(self, particles):
        pass


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
                    particles.append(Particle(random.randint(10, 40), 50, pos[0], pos[1]))
        # if count % 70 == 0:
        #     particles.append(Particle(20, 50, 50, 50, initial_x_velocity=random.randint(1, 6)))

        screen.fill((0, 0, 0))

        for i in range(len(particles)):
            particles[i].apply_gravity()
            particles[i].apply_friction_x(0.99)
            # particles[i].update_position()
            # for j in range(i, len(particles)):
            # disp = particles[i].position - particles[j].position
            # print(disp)
            # print(disp, disp.length())
            # WORKS ONLY IF PARTICLES OF SAME RADIUS
            # if disp.length() < particles[i].radius + particles[j].radius:
            # particles[j].position += math.Vector2(particles[i].radius, particles[i].radius) - disp
            particles[i].update_position()
            particles[i].stay_in_window()
            particles[i].render(screen)
            print(particles[i].velocity)
        pygame.display.update()

except KeyboardInterrupt:
    pygame.quit()
