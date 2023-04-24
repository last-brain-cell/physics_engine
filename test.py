import pygame
import pandas as pd

# initialize Pygame
pygame.init()

# set the screen size
screen_width = 400
screen_height = 400
FPS = 60
screen = pygame.display.set_mode((screen_width, screen_height))

# set the particle position
particle_x = screen_width // 2
particle_y = 20

# set the particle radius and color
particle_radius = 20
particle_color = (255, 255, 255)

# set the gravity and speed of the particle
gravity = 0.098
particle_speed = 0
click_velocity = 10

# set the game loop
running = True
velocity_data = [0]

clock = pygame.time.Clock()

while running:
    dt = clock.tick(FPS) / 60

    # fill the screen with black color
    screen.fill((0, 0, 0))

    # draw the particle
    pygame.draw.circle(screen, particle_color, (particle_x, particle_y), particle_radius)

    # check if the particle goes off the screen
    if particle_y < screen_height - particle_radius:
        particle_speed += gravity * dt
        particle_y += particle_speed
    elif particle_x > screen_width - particle_radius:
        particle_x = screen_width - particle_radius
    elif screen_width < 20:
        particle_x = 20
    else:
        particle_speed = 0
        particle_y = screen_height - particle_radius

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                particle_x, particle_y = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]
                particle_speed = 0
                print("Left Click Position" + str(pygame.mouse.get_pos()))

    if particle_speed != 0:
        print("Particle Speed: " + str(particle_speed))
        velocity_data.append(particle_speed)

    # update the screen

    # print((particle_x, particle_y))
    pygame.display.update()

data = pd.DataFrame(velocity_data)
data.to_csv("velocity_data.txt", index=False)

# quit Pygame
pygame.quit()
