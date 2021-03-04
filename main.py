from Shapes.Segment import Segment
from Shapes.Ball import Ball
import Shapes
import PIDController
import pygame

# 10 works
PIDController.K_P = 7

target_pos = (450, 650)

Shapes.add_point(target_pos)

ball = None
def onUpdate():
    pos = ball.shape.body.position
    diff = target_pos - pos
    out = PIDController.calc(diff[0])
    ball.shape.body.apply_force_at_local_point((out, 0))

ball = Shapes.add(Ball())
ball.update = onUpdate

floor = Shapes.add(Segment((-10, 700), (910, 700), 2))

Shapes.start()

