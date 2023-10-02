import pygame
from settings import Settings
from src.ship import Ship
import src.game_functions as gf


def run_game():
    # Initialize game and create screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make a ship
    ship = Ship(ai_settings, screen)

    while True:
        gf.check_events(ship)
        gf.update_screen(ai_settings, screen, ship)
        ship.update()


if __name__ == "__main__":
    run_game()
