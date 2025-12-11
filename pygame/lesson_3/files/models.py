import pygame


class Player:
    def __init__(
        self,
        p_initial_x,
        p_initial_y,
        p_width,
        p_height,
        p_speed,
        p_color=(0, 255, 0),
        p_vx=0,
        p_vy=0,
    ):
        self.rect = pygame.Rect(p_initial_x, p_initial_y, p_width, p_height)
        self._speed = p_speed
        self._max_speed = 10
        self._color = p_color
        self._vx = p_vx
        self._vy = p_vy

    def _move(self):
        """Move the Player by vx and vy"""
        self.rect.x = self.rect.x + self._vx
        self.rect.y = self.rect.y + self._vy

    def _draw(self, screen):
        """Draw the Player on the screen"""
        pygame.draw.rect(screen, self._color, self.rect)

    def get_speed(self):
        return self._speed

    def update(self, screen):
        """Move and draw the Player"""
        self._move()
        self._draw(screen)

    def set_velocity(self, p_vx, p_vy):
        """Change velocities"""
        self._vx = p_vx
        self._vy = p_vy

    def reset_position(self):
        """Reset player to its starting position"""
        # TODO: implement this for the modify task
        pass

    def increase_speed(self, amount):
        """Increase speed by given amount, capped at max speed"""
        # TODO: implement this for the modify task
        pass
