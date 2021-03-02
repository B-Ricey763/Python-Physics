import sys
import pymunk
import pygame
from pygame import *
from pymunk import body
from pymunk.shapes import Shape

def create_circle(space):
    body = pymunk.Body(0, 0, body_type = pymunk.Body.DYNAMIC)
    body.position = (400, 0)

    circ = pymunk.Circle(body, RADIUS)
    circ.mass = 10

    space.add(body, circ)

    return circ

def create_floor(space):
    body = pymunk.Body(0, 0, body_type = pymunk.Body.STATIC)

    box = pymunk.Segment(body, (0, 700), (800, 700), 2)
    
    space.add(body, box)

    return box

def draw_circles(circs):
    for circ in circs:
        pos_x = int(circ.body.position.x)
        pox_y = int(circ.body.position.y)

        pygame.draw.circle(screen, BODY_COLOR, (pos_x, pox_y), RADIUS)

def draw_floor(box):
    pos1 = (int(box.a[0]), int(box.a[1]))
    pos2 = (int(box.b[0]), int(box.b[1]))

    pygame.draw.line(screen, BODY_COLOR, pos1, pos2, 2)

pygame.init()

SIZE = 800, 800
FILL_COLOR = 200, 200, 200
BODY_COLOR = 0, 0, 0
RADIUS = 80

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
space = pymunk.Space()
space.gravity = 0, 500

circs = []
circs.append(create_circle(space))

floor = create_floor(space)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(FILL_COLOR)
    draw_circles(circs)
    draw_floor(floor)
    space.step(1/50)
    pygame.display.update()
    clock.tick(120)
            