import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullets from the ship"""

    def __init__(self, ai_settings, screen, ship):
        """Create a bullet object at the ship's current position"""
        super().__init__()
        self.screen = screen

        # create a bullet rect at (0, 0) ab=nd then set its correct position
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # store the bullet's position as a decimal value.
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
