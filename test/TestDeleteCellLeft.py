#!/usr/bin/env python
#encoding: utf-8

from PyQt4.QtGui import QWidget,QTableWidget,QTableWidgetItem,QApplication,QTableWidgetSelectionRange
from PyQt4.QtCore import Qt, QString
from PyQt4.QtTest import QTest
import unittest
import sys
sys.path.append("..")
import main
import random
from view.MainWindow import MainWindow
from view.Utils import initParent

class mytest(unittest.TestCase): 
    def setUp(self):
        self.main = MainWindow()
        self.inittablewidget = self.main.microcodeTableWidget
        #self.inittablewidget.setSelectionMode(QAbstractItemView.ContiguousSelection)

    def tearDown(self):
        self.main = None
        self.inittablewidget = None
 
    def testDeleteLeftCell(self):
        self.main.newFile()
        selrange = QTableWidgetSelectionRange(0,0,0,0)
        self.inittablewidget.setRangeSelected(selrange,True)
        self.inittablewidget.currentColumnNum = selrange.columnCount() 
        self.inittablewidget.currentLeftColumn = selrange.leftColumn()
        for i in range(0,19):
            self.inittablewidget.insertColumns()
        selrange = QTableWidgetSelectionRange(0,0,0,19)
        self.inittablewidget.setRangeSelected(selrange, False)
        self.inittablewidget.setItem(1,1,QTableWidgetItem("R0.M[0]->M[0]"))
        self.inittablewidget.setItem(1,2,QTableWidgetItem("R0.M[0]->M[1]"))
        self.inittablewidget.setItem(1,3,QTableWidgetItem("R0.M[0]->M[2]"))
        selrange = QTableWidgetSelectionRange(1,2,1,2)
        self.inittablewidget.setRangeSelected(selrange,True)
        self.inittablewidget.currentRowNum = selrange.rowCount() 
        self.inittablewidget.currentTopRow = selrange.topRow()
        self.inittablewidget.currentColumnNum = selrange.columnCount()
        self.inittablewidget.currentLeftColumn = selrange.leftColumn()
        self.inittablewidget.deleteCellLeft()
        #self.inittablewidget.setRangeSelected(selrange, False)
        self.result = self.inittablewidget.item(1,2).text()
        self.results = self.inittablewidget.item(1,3).text()
        self.expectresult = QString("R0.M[0]->M[2]")
        self.expectresults = QString("")
        self.assertEqual(self.result,self.expectresult)
        self.assertEqual(self.results,self.expectresults)

    def testDeleteLeftCell_0(self):
        self.main.newFile()
        selrange = QTableWidgetSelectionRange(0,0,0,0)
        self.inittablewidget.setRangeSelected(selrange,True)
        self.inittablewidget.currentColumnNum = selrange.columnCount() 
        self.inittablewidget.currentLeftColumn = selrange.leftColumn()
        for i in range(0,19):
            self.inittablewidget.insertColumns()
        selrange = QTableWidgetSelectionRange(0,0,0,19)
        self.inittablewidget.setRangeSelected(selrange, False)
        row = random.randint(0,1999)
        column = random.randint(0,19)
        self.inittablewidget.setItem(row, column - 1, QTableWidgetItem("R0.M[0]->M[0]"))
        self.inittablewidget.setItem(row, column, QTableWidgetItem("R0.M[0]->M[1]"))
        self.inittablewidget.setItem(row, column + 1, QTableWidgetItem("R0.M[0]->M[2]"))
        selrange = QTableWidgetSelectionRange(row, column, row , column )
        self.inittablewidget.setRangeSelected(selrange,True)
        self.inittablewidget.currentRowNum = selrange.rowCount() 
        self.inittablewidget.currentTopRow = selrange.topRow()
        self.inittablewidget.currentColumnNum = selrange.columnCount() 
        self.inittablewidget.currentLeftColumn = selrange.leftColumn()
        self.inittablewidget.deleteCellLeft()
        #self.inittablewidget.setRangeSelected(selrange, False)
        self.result = self.inittablewidget.item(row, column).text()
        self.results = self.inittablewidget.item(row, column + 1).text()
        self.expectresult = QString("R0.M[0]->M[2]")
        self.expectresults = QString("")
        self.assertEqual(self.result,self.expectresult)
        self.assertEqual(self.results,self.expectresults)

suite = unittest.TestLoader().loadTestsFromTestCase(mytest)
unittest.TextTestRunner(verbosity=2).run(suite)
