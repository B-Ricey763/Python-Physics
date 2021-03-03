import pymunk
import pygame

class Ball():
    """A dynamic circle with rendering and physics"""
    def __init__(self, space: pymunk.Space, pos: "tuple[float, float]"=(0, 0),
                 mass: float=10, radius: float=50) -> None:
        """Constructs a ball object in the given space, with given fields"""
        self.color = (0, 0, 0)
        self.radius = radius
        self.shape = self._add_physics(space, pos, mass)

    def _add_physics(self, space, pos, mass) -> pymunk.Circle:
        """Generates the physics body and shape need for pymunk"""
        body = pymunk.Body(0, 0, body_type = pymunk.Body.DYNAMIC)
        body.position = pos
        circle = pymunk.Circle(body, self.radius)
        circle.mass = mass
        space.add(body, circle)
        return circle

    def draw(self, screen) -> None:
        """Renders the ball to the screen using pygame"""
        pos = self.shape.body.position
        int_pos = (int(pos.x), int(pos.y))
        pygame.draw.circle(screen, self.color, int_pos, self.radius)