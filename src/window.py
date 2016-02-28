import pygame
from src.constants import Constants

class Window(object):

    def __init__(self, localeHandler):
        # Create surface of (width, height), and its window.
        mainSurface = pygame.display.set_mode((Constants.WIDTH, Constants.HEIGHT))
        topSeparatorLine    =   (0,
                                Constants.TOP_SEPARATION_HEIGHT,
                                Constants.WIDTH,
                                Constants.BORDER_LINE_WIDTH)
        leftSeparatorLine   =   (0,
                                Constants.TOP_SEPARATION_HEIGHT + Constants.BORDER_LINE_WIDTH,
                                Constants.BORDER_LINE_WIDTH,
                                Constants.HEIGHT)
        rightSeparatorLine  =   (Constants.WIDTH - Constants.BORDER_LINE_WIDTH,
                                Constants.TOP_SEPARATION_HEIGHT + Constants.BORDER_LINE_WIDTH,
                                Constants.BORDER_LINE_WIDTH,
                                Constants.HEIGHT)
        bottomSeparatorLine =   (0,
                                Constants.HEIGHT - Constants.BORDER_LINE_WIDTH,
                                Constants.WIDTH,
                                Constants.BORDER_LINE_WIDTH)

        whiteColor = (255, 255, 255)
        blackColor = (133, 133, 133)

        # So first fill everything with the background color
        mainSurface.fill((211, 211, 211))
        mainSurface.fill(blackColor, topSeparatorLine)
        mainSurface.fill(blackColor, leftSeparatorLine)
        mainSurface.fill(blackColor, rightSeparatorLine)
        mainSurface.fill(blackColor, bottomSeparatorLine)

        #Drawing the game grid

        #Drawing the rows
        for x in range(0, (Constants.HEIGHT - Constants.TOP_SEPARATION_HEIGHT - Constants.BORDER_LINE_WIDTH) / 10):
            rowSeparationLine =  (Constants.BORDER_LINE_WIDTH,
                                  Constants.TOP_SEPARATION_HEIGHT + Constants.BORDER_LINE_WIDTH + (x * 10),
                                  Constants.WIDTH-(2*Constants.BORDER_LINE_WIDTH),
                                  2)
            mainSurface.fill(whiteColor, rowSeparationLine)

        #Drawing the columns
        for x in range(0, Constants.WIDTH / 10 -1):
            columnSeparationLine =  (Constants.BORDER_LINE_WIDTH + (x * 10) ,
                                     Constants.TOP_SEPARATION_HEIGHT + Constants.BORDER_LINE_WIDTH,
                                     2,
                                     Constants.HEIGHT - Constants.TOP_SEPARATION_HEIGHT - (2*Constants.BORDER_LINE_WIDTH))
            mainSurface.fill(whiteColor, columnSeparationLine)

        pygame.display.set_caption(localeHandler.getString("PYGAME_WINDOW_TITLE"))
        pygame.mouse.set_visible(1)
