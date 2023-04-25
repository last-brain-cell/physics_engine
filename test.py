# import pygame
# import pandas as pd
#
# # initialize Pygame
# pygame.init()
#
# # set the screen size
# screen_width = 400
# screen_height = 400
# FPS = 60
# screen = pygame.display.set_mode((screen_width, screen_height))
#
# # set the particle position
# particle_x = screen_width // 2
# particle_y = 20
#
# # set the particle radius and color
# particle_radius = 20
# particle_color = (255, 255, 255)
#
# # set the gravity and speed of the particle
# gravity = 0.098
# particle_speed = 0
# click_velocity = 10
#
# # set the game loop
# running = True
# velocity_data = [0]
#
# clock = pygame.time.Clock()
#
# while running:
#     dt = clock.tick(FPS) / 60
#
#     # fill the screen with black color
#     screen.fill((0, 0, 0))
#
#     # draw the particle
#     pygame.draw.circle(screen, particle_color, (particle_x, particle_y), particle_radius)
#
#     # check if the particle goes off the screen
#     if particle_y < screen_height - particle_radius:
#         particle_speed += gravity * dt
#         particle_y += particle_speed
#     elif particle_x > screen_width - particle_radius:
#         particle_x = screen_width - particle_radius
#     elif screen_width < 20:
#         particle_x = 20
#     else:
#         particle_speed = 0
#         particle_y = screen_height - particle_radius
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             if pygame.mouse.get_pressed()[0]:
#                 particle_x, particle_y = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]
#                 particle_speed = 0
#                 print("Left Click Position" + str(pygame.mouse.get_pos()))
#
#     if particle_speed != 0:
#         print("Particle Speed: " + str(particle_speed))
#         velocity_data.append(particle_speed)
#
#     # update the screen
#
#     # print((particle_x, particle_y))
#     pygame.display.update()
#
# data = pd.DataFrame(velocity_data)
# data.to_csv("velocity_data.txt", index=False)
#
# # quit Pygame
# pygame.quit()

import pygame
import math

wScreen = 1200
hScreen = 500

win = pygame.display.set_mode((wScreen,hScreen))
pygame.display.set_caption('Projectile Motion')


class ball(object):
    def __init__(self,x,y,radius,color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def draw(self, win):
        pygame.draw.circle(win, (0,0,0), (self.x,self.y), self.radius)
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius-1)


    @staticmethod
    def ballPath(startx, starty, power, ang, time):
        angle = ang
        velx = math.cos(angle) * power
        vely = math.sin(angle) * power

        distX = velx * time
        distY = (vely * time) + ((-4.9 * (time ** 2)) / 2)

        newx = round(distX + startx)
        newy = round(starty - distY)


        return (newx, newy)


def redrawWindow():
    win.fill((64,64,64))
    golfBall.draw(win)
    pygame.draw.line(win, (0,0,0),line[0], line[1])
    pygame.display.update()

def findAngle(pos):
    sX = golfBall.x
    sY = golfBall.y
    try:
        angle = math.atan((sY - pos[1]) / (sX - pos[0]))
    except:
        angle = math.pi / 2

    if pos[1] < sY and pos[0] > sX:
        angle = abs(angle)
    elif pos[1] < sY and pos[0] < sX:
        angle = math.pi - angle
    elif pos[1] > sY and pos[0] < sX:
        angle = math.pi + abs(angle)
    elif pos[1] > sY and pos[0] > sX:
        angle = (math.pi * 2) - angle

    return angle


golfBall = ball(300,494,5,(255,255,255))

run = True
time = 0
power = 0
angle = 0
shoot = False
clock = pygame.time.Clock()
while run:
    clock.tick(200)
    if shoot:
        if golfBall.y < 500 - golfBall.radius:
            time += 0.05
            po = ball.ballPath(x, y, power, angle, time)
            golfBall.x = po[0]
            golfBall.y = po[1]
        else:
            shoot = False
            time = 0
            golfBall.y = 494

    line = [(golfBall.x, golfBall.y), pygame.mouse.get_pos()]
    redrawWindow()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if not shoot:
                x = golfBall.x
                y = golfBall.y
                pos =pygame.mouse.get_pos()
                shoot = True
                power = math.sqrt((line[1][1]-line[0][1])**2 +(line[1][0]-line[0][1])**2)/8
                angle = findAngle(pos)



pygame.quit()
quit()








































































































































































































































































































































































































































































































































































































