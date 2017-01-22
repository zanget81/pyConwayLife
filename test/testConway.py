__author__ = 'angel'

import unittest
from src.conway import Conway

class Test(unittest.TestCase):

    def testConwayUpdateListOfActiveCells(self):
        listOfPos = [(1,1), (3,3), (5,5), (7,7), (7,8), (7,6)]
        conwayModel = Conway()
        conwayModel.updateListOfActiveCells(listOfPos)
        self.assertEqual(conwayModel.listOfActiveCellsPos, listOfPos)

    def testConwayApplyKillingRulesUnderpopulated(self):
        listOfPos = [(1,1), (3,3), (5,5), (7,7), (7,8), (6,7)]
        conwayModel = Conway()
        conwayModel.updateListOfActiveCells(listOfPos)
        conwayModel.applyKillingRules()
        self.assertEqual(conwayModel.listOfActiveCellsPos, [(7,7), (7,8), (6,7)])

    def testConwayApplyKillingRulesOverpopulated(self):
        listOfPos = [(3,3), (3,4), (4,3), (3,2), (2,3)]
        conwayModel = Conway()
        conwayModel.updateListOfActiveCells(listOfPos)
        conwayModel.applyKillingRules()
        self.assertEqual(conwayModel.listOfActiveCellsPos, [(3,4), (4,3), (3,2), (2,3)])

    def testConwayUpdateModel(self):
        listOfPos = [(3,3), (3,4), (4,3), (3,2), (2,3)]
        conwayModel = Conway()
        conwayModel.updateListOfActiveCells(listOfPos)
        conwayModel.updateModel()
        self.assertEqual(conwayModel.listOfActiveCellsPos, [(3,4), (4,3), (3,2), (2,3)])