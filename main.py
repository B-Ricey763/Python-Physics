import sys
import pymunk
import pygame
from pygame import *

def create_circ(space, pos, mass):
    body = pymunk.Body(0, 0, body_type = pymunk.Body.DYNAMIC)
    body.position = pos
    circ = pymunk.Circle(body, RADIUS)
    circ.mass = mass
    space.add(body, circ)
    return circ

def create_static_seg(space, ptA, ptB, width):
    body = pymunk.Body(0, 0, body_type = pymunk.Body.STATIC)
    seg = pymunk.Segment(body, ptA, ptB, width)
    space.add(body, seg)
    return seg

def draw_circs(circs):
    for circ in circs:
        pos_x = int(circ.body.position.x)
        pox_y = int(circ.body.position.y)

        pygame.draw.circle(screen, BODY_COLOR, (pos_x, pox_y), RADIUS)

def draw_floor(seg):
    pos1 = (int(seg.a[0]), int(seg.a[1]))
    pos2 = (int(seg.b[0]), int(seg.b[1]))
    pygame.draw.line(screen, BODY_COLOR, pos1, pos2, 2)

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

circs = []
circs.append(create_circ(space, (400, 0), 10))

floor = create_static_seg(space, 
    (0, SIZE[1] - 10), (SIZE[0], SIZE[1] - 10), 
    2)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(FILL_COLOR)
    draw_circs(circs)
    draw_floor(floor)
    space.step(1/50)
    pygame.display.update()
    clock.tick(120)
            