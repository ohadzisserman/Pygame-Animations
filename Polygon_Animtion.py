import pygame
from time import sleep
from math import sin, cos, pi
import random

# initialize Pygame
pygame.init()

# set up screen dimensions
SCREEN_WIDTH = 850
SCREEN_HEIGHT = 850

# set up screen center and radius
SCREEN_CENTER = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 40]
SCREEN_RADIUS = (2 / 5) * min(SCREEN_WIDTH, SCREEN_HEIGHT)

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# create screen object
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
SCREEN.fill(BLACK)
pygame.display.flip()

# set up font
FONT = pygame.font.SysFont(None, 45)

def draw_polygon(n):
    """
    Draws a polygon with n sides on the screen using Pygame.
    """
    # render text for number of sides
    sides_text = FONT.render(str(n), True, WHITE)

    # draw number of sides at the top center of screen
    SCREEN.blit(sides_text, [SCREEN_WIDTH // 2, 50])

    # calculate vertex coordinates using trigonometry
    vertices = [[SCREEN_CENTER[0] + SCREEN_RADIUS * cos(i * 2 * pi / n), SCREEN_CENTER[1] + SCREEN_RADIUS * sin(i * 2 * pi / n)] for i in range(n)]

    # draw vertices as small red circles
    for vertex in vertices:
        pygame.draw.circle(SCREEN, random.choice(range(256)), vertex, 5)

    # draw lines between vertices to form polygon with random colors
    for i in range(len(vertices)):
        for j in range(len(vertices)):
            # pygame.draw.line(SCREEN, (random.choice(range(256)),random.choice(range(256)),random.choice(range(256))), vertices[i], vertices[j])
             pygame.draw.line(SCREEN, (255,255,255), vertices[i], vertices[j])

    # update screen
    pygame.display.flip()

# draw polygons with increasing number of sides
for n in range(3, 100):
    SCREEN.fill(BLACK)
    draw_polygon(n)
    sleep(0.5)

# draw polygons with decreasing number of sides and increasing delay
for n in range(2, 10):
    SCREEN.fill(BLACK)
    draw_polygon(n)
    sleep(0.5)

for n in range(10, 41, 3):
    SCREEN.fill(BLACK)
    draw_polygon(n)
    sleep(0.5)
