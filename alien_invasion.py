import sys
import pygame
from settings import Settings
from src.ship import Ship

def run_game():
    # Initialize game and create screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make a ship
    ship = Ship(screen)
    # set the background color
    # bg_color = (230, 230, 230)
    # Start the main loop for the game.
    while True:

        # Watch for keyboad and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # redraw the screen during each pass through the loop
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        # Make the most recent drawn screen visible.
        pygame.display.flip()


if __name__ == "__main__":
    run_game()
