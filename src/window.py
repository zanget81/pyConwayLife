import pygame
from src.constants import Constants

class Window(object):
    mainSurface = None
    tableOfEnabledCells = {}
    cellMap = None
    WINDOW_UPDATE_ID = pygame.USEREVENT + 1

    def __init__(self, localeHandler):
        # Create surface of (width, height), and its window.
        self.mainSurface = pygame.display.set_mode((Constants.WIDTH, Constants.HEIGHT))
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

        # So first fill everything with the background color
        self.mainSurface.fill(Constants.UNSELECTED_CELL_COLOR)
        self.mainSurface.fill(Constants.SELECTED_CELL_COLOR, topSeparatorLine)
        self.mainSurface.fill(Constants.SELECTED_CELL_COLOR, leftSeparatorLine)
        self.mainSurface.fill(Constants.SELECTED_CELL_COLOR, rightSeparatorLine)
        self.mainSurface.fill(Constants.SELECTED_CELL_COLOR, bottomSeparatorLine)

        rows = range(0, (Constants.HEIGHT - Constants.TOP_SEPARATION_HEIGHT - Constants.BORDER_LINE_WIDTH) / 10)
        cols = range(0, Constants.WIDTH / 10 -1)
        self.cellMap = [[0 for y in cols] for x in rows]

        #Drawing the rows
        for x in rows:
            rowSeparationLine =  (Constants.BORDER_LINE_WIDTH,
                                  Constants.TOP_SEPARATION_HEIGHT + Constants.BORDER_LINE_WIDTH + (x * 10),
                                  Constants.WIDTH-(2*Constants.BORDER_LINE_WIDTH),
                                  Constants.SEPARATION_LINE_WIDTH)
            self.mainSurface.fill(whiteColor, rowSeparationLine)

        #Drawing the columns
        for x in cols:
            columnSeparationLine =  (Constants.BORDER_LINE_WIDTH + (x * 10) ,
                                     Constants.TOP_SEPARATION_HEIGHT + Constants.BORDER_LINE_WIDTH,
                                     Constants.SEPARATION_LINE_WIDTH,
                                     Constants.HEIGHT - Constants.TOP_SEPARATION_HEIGHT - (2*Constants.BORDER_LINE_WIDTH))
            self.mainSurface.fill(whiteColor, columnSeparationLine)

        for x in rows:
            for y in cols:
                self.cellMap[x][y] = (Constants.BORDER_LINE_WIDTH + (x * 10),
                                      Constants.TOP_SEPARATION_HEIGHT + Constants.BORDER_LINE_WIDTH + (y * 10))

        pygame.display.set_caption(localeHandler.getString("PYGAME_WINDOW_TITLE"))
        pygame.mouse.set_visible(1)

    def __isACell(self, pos):
        cell = ()

        for x in range(0, (Constants.HEIGHT - Constants.TOP_SEPARATION_HEIGHT - Constants.BORDER_LINE_WIDTH) / 10):
            posXLine = Constants.TOP_SEPARATION_HEIGHT + Constants.BORDER_LINE_WIDTH + (x * 10)
            posXNextLine = Constants.TOP_SEPARATION_HEIGHT + Constants.BORDER_LINE_WIDTH + ((x+1) * 10)

            if ((pos[1] >= (posXLine + Constants.SEPARATION_LINE_WIDTH)) and
                (pos[1] <= posXNextLine)):
                cell = (0, (posXLine + Constants.SEPARATION_LINE_WIDTH), 8, 8)

        for y in range(0, Constants.WIDTH / 10 -1):
            posYLine = Constants.BORDER_LINE_WIDTH + (y * 10)
            posYNextLine = Constants.BORDER_LINE_WIDTH + ((y+1) * 10)

            if ((pos[0] >= (posYLine + Constants.SEPARATION_LINE_WIDTH)) and
                (pos[0] <= posYNextLine) and
                cell):
                    cell = ((posYLine + Constants.SEPARATION_LINE_WIDTH), cell[1], 8, 8)

        return cell if (cell and (cell[0] > 0) and (cell[1] > 0)) else ()


    def toggleCell(self, pos):
        self.mainSurface.fill((12, 133, 255), (pos[0], pos[1], 1, 1))
        selectedCell = self.__isACell(pos)

        if (selectedCell):
            key = str(selectedCell[0]) + str(selectedCell[1])
            if (self.tableOfEnabledCells.get(key)):
                del self.tableOfEnabledCells[key]
                self.mainSurface.fill(Constants.UNSELECTED_CELL_COLOR, selectedCell)
            else:
                self.tableOfEnabledCells[key] = selectedCell
                self.mainSurface.fill(Constants.SELECTED_CELL_COLOR, selectedCell)

    def setWindowUpdateSpeed(self, time):
        pygame.time.set_timer(self.WINDOW_UPDATE_ID, time)

    def updateWindow(self):
        pass
