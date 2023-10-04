class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's settings."""

        # screen settings
        self.screen_width = 1320
        self.screen_height = 720
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed_factor = 5.0

        # Bullet settings
        self.bullet_speed = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 7

        # Alien settings
        self.alien_speed = 1
        self.drop_speed = 10
        # fleet direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

