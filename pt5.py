import pygame
import math
from math import *

pygame.init()

BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (0,0, 255)


size = (700 , 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Professor Craven's Cool Game")

done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(WHITE)
    # pygame.draw.rect(screen, RED, (55,50,20,25))
    # pygame.draw.line(screen, GREEN, [0,0],[100, 100], 5)
    y_offset = 0
    # while y_offset<100:
    #     pygame.draw.line(screen,RED,[0,10+y_offset],[100,110+y_offset],5)
    #     y_offset = y_offset + 10

    # for y_offset in range(0, 100, 10):
    #     pygame.draw.line(screen,RED,[0,10+y_offset],[100,110+y_offset],5)

    # for i in range(200):
    #     radians_x = i / 20
    #     radians_y = i / 6
    #
    #     x = int(75 * math.sin(radians_x)) + 200
    #     y = int(75 * math.sin(radians_y)) + 200
    #
    #     pygame.draw.line(screen, BLACK, [x,y], [x+5, y ], 5)
    #
    # for x_offset in range(30, 300, 30):
    #     pygame.draw.line(screen,BLACK,[x_offset,100],[x_offset-10,90],2)
    #     pygame.draw.line(screen,BLACK,[x_offset,90],[x_offset-10,100],2)

    # pygame.draw.rect(screen, BLACK, [20,20,250,100],0)
    # pygame.draw.ellipse(screen, BLACK, [20,20,250,100,],2)
    # pygame.draw.arc(screen, GREEN,[100,100,250,200], pi/2, pi, 2)
    # pygame.draw.arc(screen, BLACK,[100,100,250,200], 0, pi/2, 2)
    # pygame.draw.arc(screen, RED,[100,100,250,200], 3*pi/2, 2*pi, 2)
    # pygame.draw.arc(screen, BLACK,[100,100,250,200], pi, 3*pi/2, 2)
    # pygame.draw.polygon(screen, BLACK, [[100,100], [0,200], [200,200]], 5)

    font = pygame.font.SysFont('Calibri', 25, True, False)

    text = font.render("My text", True, BLACK)

    screen.blit(text, [250,250])


    pygame.display.flip()
    clock.tick(60)

pygame.quit()