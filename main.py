import sys
import pymunk
import pygame
from Shapes.Ball import Ball
from Shapes.Segment import Segment

SIZE = 900, 900
FILL_COLOR = 200, 200, 200
BODY_COLOR = 0, 0, 0
RADIUS = 80
GRAVITY = 100

pygame.init()

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
space = pymunk.Space()
space.gravity = 0, GRAVITY

shapes = []
shapes.append(Ball(space, (400, 0)))
shapes.append(Segment(space, (0, 500), (900, 700), 2))

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(FILL_COLOR)
    
    for shape in shapes:
        shape.draw(screen)
    space.step(1/50)
    pygame.display.update()
    clock.tick(120)
            