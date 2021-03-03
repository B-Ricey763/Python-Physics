import pygame
import pymunk

class Segment():
    """A static line with rendering and physics"""
    def __init__(self, space, ptA, ptB, width) -> None:
        """Constructs a line object in the given space, with given fields"""
        self.color = (0, 0, 0)
        self.width = width
        self.shape = self._add_physics(space, ptA, ptB)

    def _add_physics(self, space, ptA, ptB) -> pymunk.Segment:
        """Generates the physics body and shape need for pymunk"""
        body = pymunk.Body(0, 0, body_type = pymunk.Body.STATIC)
        seg = pymunk.Segment(body, ptA, ptB, self.width)
        space.add(body, seg)
        return seg

    def draw(self, screen) -> None:
        """Renders the ball to the screen using pygame"""
        seg = self.shape
        pos1 = (int(seg.a[0]), int(seg.a[1]))
        pos2 = (int(seg.b[0]), int(seg.b[1]))
        pygame.draw.line(screen, self.color, pos1, pos2, self.width)