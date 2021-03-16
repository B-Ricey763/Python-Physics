from Shapes.Segment import Segment
from Shapes.Ball import Ball
import Shapes
import PIDController
import pygame

# 10 works
# PIDController.K_P = 0.1
# PIDController.K_I = 0.1
# PIDController.K_D = 0

target_pos = (640, 650)

Shapes.add_point(target_pos)

ball = None
def onUpdate():
    global ball
    pos = ball.shape.body.position
    diff = target_pos[0] - pos[0]

    # out = PIDController.calc(diff)
    ball.shape.body.apply_force_at_local_point((out, 0))

ball = Shapes.add(Ball())
ball.update = onUpdate

floor = Shapes.add(Segment((-1000, 700), (10000, 700), 2))

Shapes.start()

