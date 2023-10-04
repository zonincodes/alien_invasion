import sys
import pygame
from src.bullet import Bullet
from src.alien import Alien

def check_events(ship, ai_settings, screen, bullets):
    """Watch and respond to keyboad and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_key_down_events(event, ship, ai_settings, screen, bullets)

        elif event.type == pygame.KEYUP:
            check_key_up_events(event, ship)


def check_key_down_events(event, ship, ai_settings, screen, bullets):
    """Respond to key presses"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullets(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def check_key_up_events(event, ship):
    """Respond to key releases"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def fire_bullets(ai_settings, screen, ship, bullets):
    """Fire bullet if limit is not reached yet"""
    # create a new bullet and add it to the bullets group
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def update_bullets(bullets):
    """Update position of bullets and get rid of the old ones"""
    # update the bullets
    bullets.update()

    # remove the bullets that have disappeared
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # print(len(bullets))


def create_fleet(ai_settings, screen, aliens):
    """Create a full fleet of aliens"""

    # create an alien and find the number of aliens in a row
    # Spacing between each alien is equal to one alien width
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))

    # create the first row og aliens
    for alien_number in range(number_aliens_x):
        # Create an alien and place it in the row
        alien = Alien(ai_settings, screen)
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        aliens.add(alien)


def update_screen(ai_settings, screen, ship, bullets, aliens):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    # Redraw all bullets behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # show alien ship
    aliens.draw(screen)
    # Make the most recent drawn screen visible.
    pygame.display.flip()


