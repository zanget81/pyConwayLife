__author__ = 'angel'

import pygame

from src.constants import Constants
from src.appLocale import AppLocale


def main():

    localeHandler = AppLocale(Constants.LOCALE)
    my_clock = pygame.time.Clock()
    frameCounter = 0

    """ Set up the game and run the main game loop """
    pygame.init()  # Prepare the pygame module for use

    # Create surface of (width, height), and its window.
    mainSurface = pygame.display.set_mode((Constants.WIDTH, Constants.HEIGHT))

    pygame.display.set_caption(localeHandler.getString("PYGAME_WINDOW_TITLE"))
    pygame.mouse.set_visible(1)

    while True:
        ev = pygame.event.poll()    # Look for any event
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break                   #   ... leave game loop
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            break

        pygame.display.update()

        #force a constant frame rate of 60fps
        my_clock.tick(Constants.FRAME_RATE)

    pygame.quit()     # Once we leave the loop, close the window.

if __name__ == "__main__":
    main()
