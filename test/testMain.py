# -*- coding: utf-8 -*-
'''
Created on May 04, 2016

@author: litt 
'''

from PyQt4.QtGui import QWidget, QTableWidget, QTableWidgetItem, QApplication, QTableWidgetSelectionRange, QAbstractItemView, QBrush, QColor, QApplication
from PyQt4.QtCore import Qt, QString, QStringList
from PyQt4.QtTest import QTest
import unittest
import sys 
sys.path.append("..")
import random
from view.MainWindow import MainWindow
from view.Utils import initParent


class TestOutput(unittest.TestCase): 
    def setUp(self):

        self.mainWindow = None
        self.inittablewidget = None
        
    def tearDown(self):
        self.mainWindow = None
        self.inittablewidget = None

    def test(self):
        app = QApplication(sys.argv)
        self.mainWindow = MainWindow()
        self.inittablewidget = self.mainWindow.microcodeTableWidget
        self.mainWindow.newFile()

        textList = ["r0.m[0]->m[0]", "t0+t0(t)->biu0", "shu0.t2 ind tbh(tb=+2)->ialu.t1(i0)", "double t0(t)->biu0"]
        for k in xrange(1):
	    row  = 0
	    column = 0
            for i in xrange(1):
		selranges = QTableWidgetSelectionRange(row, column, row + 3 , column)
		self.inittablewidget.setRangeSelected(selranges, True)	
		QTest.keyClicks(self.mainWindow.register0Text, "1")
		QTest.mouseClick(self.mainWindow.register0Check, Qt.LeftButton)
		QTest.keyClicks(self.mainWindow.register1Text, "2")
		QTest.mouseClick(self.mainWindow.register1Check, Qt.LeftButton)
		QTest.keyClicks(self.mainWindow.register2Text, "3")
		QTest.mouseClick(self.mainWindow.register2Check, Qt.LeftButton)
		QTest.keyClicks(self.mainWindow.register3Text, "4")
		QTest.mouseClick(self.mainWindow.register3Check, Qt.LeftButton)
		
		self.inittablewidget.setRangeSelected(selranges, False)
         
        self.inittablewidget.saveFile("test.mpu.s")
        self.mainWindow.show()
        app.exec_()

suite = unittest.TestLoader().loadTestsFromTestCase(TestOutput)
unittest.TextTestRunner(verbosity=2).run(suite)
