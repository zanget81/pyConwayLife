
MIN_NEIGHBOURS_NEEDED_TO_SURVIVE = 2

class Conway(object):
    listOfActiveCellsPos = []

    def updateListOfActiveCells(self, newActiveList):
        self.listOfActiveCellsPos = newActiveList

    def updateModel(self):
        self.applyRule1()

    def applyRule1(self):
        removeList = []
        for cellPos in self.listOfActiveCellsPos:
            rightNeighbour = (cellPos[0] + 1, cellPos[1])
            leftNeighbour = (cellPos[0] - 1, cellPos[1])
            topNeighbour = (cellPos[0], cellPos[1] - 1)
            bottomNeighbour = (cellPos[0], cellPos[1] + 1)
            topLeftNeighbour = (cellPos[0] -1, cellPos[1] - 1)
            topRightNeighbour = (cellPos[0] + 1, cellPos[1] - 1)
            bottomLeftNeighbour = (cellPos[0] -1, cellPos[1] + 1)
            bottomRightNeighbour = (cellPos[0] + 1, cellPos[1] + 1)
            neighbourCount = 0

            for NeighbourCell in self.listOfActiveCellsPos:
                if ((NeighbourCell == rightNeighbour) or
                    (NeighbourCell == leftNeighbour) or
                    (NeighbourCell == topNeighbour) or
                    (NeighbourCell == bottomNeighbour) or
                    (NeighbourCell == topLeftNeighbour) or
                    (NeighbourCell == topRightNeighbour) or
                    (NeighbourCell == bottomLeftNeighbour) or
                    (NeighbourCell == bottomRightNeighbour)):
                    neighbourCount+=1

            if  (neighbourCount < MIN_NEIGHBOURS_NEEDED_TO_SURVIVE):
                removeList.append(cellPos)

        #Remove dead cells
        for cellPos in removeList:
            self.listOfActiveCellsPos.remove(cellPos)