
MIN_NEIGHBOURS_NEEDED_TO_SURVIVE = 2
MAX_NEIGHBOURS_NEEDED_TO_SURVIVE = 3

class Conway(object):
    listOfActiveCellsPos = []

    def __getListOfNeighbour(self, cellPos):
        return [(cellPos[0] + 1, cellPos[1]),
                (cellPos[0] - 1, cellPos[1]),
                (cellPos[0], cellPos[1] - 1),
                (cellPos[0], cellPos[1] + 1),
                (cellPos[0] - 1, cellPos[1] - 1),
                (cellPos[0] + 1, cellPos[1] - 1),
                (cellPos[0] - 1, cellPos[1] + 1),
                (cellPos[0] + 1, cellPos[1] + 1)]

    def updateListOfActiveCells(self, newActiveList):
        self.listOfActiveCellsPos = newActiveList

    #Kill underpopulated and overpopulated cells
    def applyKillingRules(self):
        removeList = []
        for cellPos in self.listOfActiveCellsPos:
            neighbourCount = 0
            lisOfNeighbours = self.__getListOfNeighbour(cellPos)
            for NeighbourCell in lisOfNeighbours:
                if (NeighbourCell in self.listOfActiveCellsPos):
                    neighbourCount+=1

            if  ((neighbourCount < MIN_NEIGHBOURS_NEEDED_TO_SURVIVE) or
                (neighbourCount > MAX_NEIGHBOURS_NEEDED_TO_SURVIVE)):
                removeList.append(cellPos)

        #Remove dead cells
        for cellPos in removeList:
            self.listOfActiveCellsPos.remove(cellPos)

    def applyReproductionRules(self):
        #for cellPos in self.listOfActiveCellsPos:
        pass


    def updateModel(self):
        self.applyKillingRules()
        self.applyReproductionRules()