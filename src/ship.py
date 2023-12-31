import pygame


class Ship:
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # start each ship at the bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a float for ships horizontal position.
        self.x = float(self.rect.x)
        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed_factor

        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed_factor

        # Update rect object from self.center.
        self.rect.x = self.x

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def blit_me(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
