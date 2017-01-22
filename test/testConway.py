__author__ = 'angel'

import unittest
from src.conway import Conway

class Test(unittest.TestCase):

    def testConwayUpdateListOfActiveCells(self):
        listOfPos = [(1,1), (3,3), (5,5), (7,7), (7,8), (7,6)]
        conwayModel = Conway()
        conwayModel.updateListOfActiveCells(listOfPos)
        self.assertEqual(conwayModel.listOfActiveCellsPos, listOfPos)

    def testConwayApplyRule1(self):
        listOfPos = [(1,1), (3,3), (5,5), (7,7), (7,8), (6,7)]
        conwayModel = Conway()
        conwayModel.updateListOfActiveCells(listOfPos)
        conwayModel.applyRule1()
        print "result: " + str(conwayModel.listOfActiveCellsPos)
        self.assertEqual(conwayModel.listOfActiveCellsPos, [(7,7), (7,8), (6,7)])