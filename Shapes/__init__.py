import sys
import pymunk
import pygame
from .Ball import Ball
from .Segment import Segment

SIZE = 900, 900
FILL_COLOR = 200, 200, 200
GRAVITY = 100


screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
space = pymunk.Space()
space.gravity = 0, GRAVITY
_shapes = []
_pts = []

def add(shape):
    _shapes.append(shape)
    return shape # for chaining

def add_point(pos):
    _pts.append(pos)

def start():
    pygame.init()

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    _shapes[0].apply_force((0, -1000))
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(FILL_COLOR)
        
        

        for shape in _shapes:
            shape.draw(screen)
            shape.update()

        for pt in _pts:
            pygame.draw.circle(screen, (0, 0, 0), pt, 3)
        space.step(1/50)
        pygame.display.update()
        clock.tick(120)


if __name__ == "__main__":
    start()