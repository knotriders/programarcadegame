import pygame
pygame.init

BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
clock = pygame.time.Clock()
done = False

SIZE = [400, 400]
screen = pygame.display.set_mode(SIZE)
def draw_snowman(screen, x, y):
    pygame.draw.ellipse(screen, WHITE, [35+x, 0+y, 25, 25])
    pygame.draw.ellipse(screen, WHITE, [23+x, 20+y, 50, 50])
    pygame.draw.ellipse(screen, WHITE, [0+x, 65+y, 100, 100])

while not done:
    screen.fill(BLACK)
    draw_snowman(screen, 100, 100)
    draw_snowman(screen, 50, 100)
    draw_snowman(screen, 70, 100)


    pygame.display.flip()
    clock.tick(20)
pygame.quit()
