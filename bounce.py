import pygame
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
pygame.display.set_caption("Bounce")
screen.fill((0, 0, 0))


class Features:
    def __init__(self):
        self.gravity = 9.8
        self.entity_speed = 0
        self.iscollided = False
        self.color = random.choice(colors)
        self.mass = None

    def activate_gravity(self):
        pass

    def float_around(self):
        pass


class Particle(Features):
    def __init__(self, x, y, radius):
        super().__init__()
        self.x = x
        self.y = y
        self.radius = radius
        self.hitbox = pygame.Rect(x - radius, y - radius, radius * 2, radius * 2)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

    def update(self):
        self.hitbox.center = (int(self.x), int(self.y))

    def check_collision(self, particles: list):
        for i in range(len(particles)):
            for j in range(i + 1, len(particles)):
                if particles[i].hitbox.colliderect(particles[j].hitbox):
                    print("Collision")
                    return True
                else:
                    return False


particles = []
for i in range(10):
    x = random.uniform(50, SCREEN_WIDTH - 50)
    y = random.uniform(50, SCREEN_HEIGHT - 50)
    radius = random.randint(10, 30)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    particle = Particle(x, y, radius)
    particles.append(particle)

# Set up game loop
running = True
while running:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen
    screen.fill((0, 0, 0))

    # Update particles
    for particle in particles:
        particle.update()

    # Check for collisions
    for i in range(len(particles)):
        for j in range(i + 1, len(particles)):
            if particles[i].hitbox.colliderect(particles[j].hitbox):
                print("Particles collided!")

    # Draw particles
    for particle in particles:
        particle.draw(screen)

    # Update screen
    pygame.display.flip()

# Quit Pygame
pygame.quit()
