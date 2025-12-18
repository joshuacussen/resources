import pygame


class Ball:
    def __init__(self, p_x, p_y, p_radius, p_color=(255, 0, 0), p_vx=0, p_vy=0):
        """Constructor"""
        # TODO: Implement constructor, storing all parameters in attributes

    def __draw(self, screen):
        """Draws the Ball on the screen"""
        # TODO: Implement!

    def __move(self):
        """Moves the Ball by vx and vy"""
        # TODO: Implement!

    def update(self, screen):
        """Move and draw the ball"""
        self.__move()
        self.__draw(screen)
