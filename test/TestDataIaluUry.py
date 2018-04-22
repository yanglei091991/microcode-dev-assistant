#!/usr/bin/env python
#encoding: utf-8

from PyQt4.QtGui import QWidget,QTableWidget,QTableWidgetItem,QApplication,QTableWidgetSelectionRange,QAbstractItemView
from PyQt4.QtCore import Qt, QString,QStringList
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
        "test IALU register read"
        self.main = MainWindow()
        self.inittablewidget = self.main.microcodeTableWidget
        global condlist
        condlist = ["","@(c)","@(!c)"]

    def tearDown(self):
        self.main = None
        self.inittablewidget = None

    def testDataIalu(self):
        self.main.newFile()
        row = random.randint(0,1999)
        column = random.randint(0,19)
        biulist = ["biu0","biu1","biu2"]
        for m in xrange(0,4):
            for biu in biulist:
                for cond in condlist:
                    text = "NOT t%s->%s%s"%(m,biu,cond)
                    #print text
                    selranges = QTableWidgetSelectionRange(row, column, row, column)
                    self.inittablewidget.setRangeSelected(selranges, True)
                    self.inittablewidget.setItem(row, column,QTableWidgetItem(text))
                    self.inittablewidget.dataParser(row, column)
                    self.assertEqual(self.inittablewidget.item(row, column).background(),self.inittablewidget.defaultBackgroundColor)
                    self.assertEqual(self.inittablewidget.database.searchMcc(self.inittablewidget.mmpulite.result), "4")


    def testDataIalu_0(self):
        self.main.newFile()
        row = random.randint(0,1999)
        column = random.randint(0,19)
        for m in xrange(0,4):
            for t in xrange(0,127):
                for cond in condlist:
                    text = "NOT t%s->m[%s]%s"%(m,t,cond)
                    #print text
                    selranges = QTableWidgetSelectionRange(row, column, row, column)
                    self.inittablewidget.setRangeSelected(selranges, True)
                    self.inittablewidget.setItem(row, column,QTableWidgetItem(text))
                    self.inittablewidget.dataParser(row, column)
                    self.assertEqual(self.inittablewidget.item(row, column).background(),self.inittablewidget.defaultBackgroundColor)
                    self.assertEqual(self.inittablewidget.database.searchMcc(self.inittablewidget.mmpulite.result), "4")


    def testDataIalu_1(self):
        self.main.newFile()
        row = random.randint(0,1999)
        column = random.randint(0,19)
        macclist = ["ialu","imac","falu"]
        for m in xrange(0,4):
            for macc in macclist:
                for t in xrange(0,4):
                    for cond in condlist:
                        text = "NOT t%s->%s.t%s%s"%(m,macc,t,cond)
                        #print text
                        selranges = QTableWidgetSelectionRange(row, column, row, column)
                        self.inittablewidget.setRangeSelected(selranges, True)
                        self.inittablewidget.setItem(row, column,QTableWidgetItem(text))
                        self.inittablewidget.dataParser(row, column)
                        self.assertEqual(self.inittablewidget.item(row, column).background(),self.inittablewidget.defaultBackgroundColor)
                        self.assertEqual(self.inittablewidget.database.searchMcc(self.inittablewidget.mmpulite.result), "3")

    def testDataIalu_2(self):
        self.main.newFile()
        row = random.randint(0,1999)
        column = random.randint(0,19)
        shulist = ["shu0","shu1"]
        for m in xrange(0,4):
            for shu in shulist:
                for t in xrange(0,4):
                    for cond in condlist:
                        text = "NOT t%s->%s.t%s%s"%(m,shu,t,cond)
                        #print text
                        selranges = QTableWidgetSelectionRange(row, column, row, column)
                        self.inittablewidget.setRangeSelected(selranges, True)
                        self.inittablewidget.setItem(row, column,QTableWidgetItem(text))
                        self.inittablewidget.dataParser(row, column)
                        self.assertEqual(self.inittablewidget.item(row, column).background(),self.inittablewidget.defaultBackgroundColor)
                        self.assertEqual(self.inittablewidget.database.searchMcc(self.inittablewidget.mmpulite.result), "4")


    def testDataIalu_3(self):
        self.main.newFile()
        row = random.randint(0,1999)
        column = random.randint(0,19)
        biulist = ["biu0","biu1","biu2"]
        bytelist = ["b","u,b"]
        dplist = ["rmax","rmin"]
        for dp in dplist:
            for m in xrange(0,4):
                for byte in bytelist:
                    for biu in biulist:
                        for cond in condlist:
                            text = "%s t%s(%s)->%s%s"%(dp,m,byte,biu,cond)
                            #print text
                            selranges = QTableWidgetSelectionRange(row, column, row, column)
                            self.inittablewidget.setRangeSelected(selranges, True)
                            self.inittablewidget.setItem(row, column,QTableWidgetItem(text))
                            self.inittablewidget.dataParser(row, column)
                            self.assertEqual(self.inittablewidget.item(row, column).background(),self.inittablewidget.defaultBackgroundColor)
                            self.assertEqual(self.inittablewidget.database.searchMcc(self.inittablewidget.mmpulite.result), "4")


    def testDataIalu_4(self):
        self.main.newFile()
        row = random.randint(0,1999)
        column = random.randint(0,19)
        bytelist = ["b","u,b"]
        dplist = ["rmax","rmin"]
        for dp in dplist:
            for m in xrange(0,4):
                for byte in bytelist:
                    for t in xrange(0,127):
                        for cond in condlist:
                            text = "%s t%s(%s)->m[%s]%s"%(dp,m,byte,t,cond)
                            #print text
                            selranges = QTableWidgetSelectionRange(row, column, row, column)
                            self.inittablewidget.setRangeSelected(selranges, True)
                            self.inittablewidget.setItem(row, column,QTableWidgetItem(text))
                            self.inittablewidget.dataParser(row, column)
                            self.assertEqual(self.inittablewidget.item(row, column).background(),self.inittablewidget.defaultBackgroundColor)
                            self.assertEqual(self.inittablewidget.database.searchMcc(self.inittablewidget.mmpulite.result), "4")


    def testDataIalu_5(self):
        self.main.newFile()
        row = random.randint(0,1999)
        column = random.randint(0,19)
        bytelist = ["b","u,b"]
        macclist = ["ialu","imac","falu"]
        dplist = ["rmax","rmin"]
        for dp in dplist:
            for m in xrange(0,4):
                for byte in bytelist:
                    for macc in macclist:
                        for t in xrange(0,4):
                            for cond in condlist:
                                text = "%s t%s(%s)->%s.t%s%s"%(dp,m,byte,macc,t,cond)
                                #print text
                                selranges = QTableWidgetSelectionRange(row, column, row, column)
                                self.inittablewidget.setRangeSelected(selranges, True)
                                self.inittablewidget.setItem(row, column,QTableWidgetItem(text))
                                self.inittablewidget.dataParser(row, column)
                                self.assertEqual(self.inittablewidget.item(row, column).background(),self.inittablewidget.defaultBackgroundColor)
                                self.assertEqual(self.inittablewidget.database.searchMcc(self.inittablewidget.mmpulite.result), "3")


    def testDataIalu_6(self):
        self.main.newFile()
        row = random.randint(0,1999)
        column = random.randint(0,19)
        shulist = ["shu0","shu1"]
        bytelist = ["b","u,b"]
        dplist = ["rmax","rmin"]
        for dp in dplist:
            for m in xrange(0,4):
                for byte in bytelist:
                    for shu in shulist:
                        for t in xrange(0,4):
                            for cond in condlist:
                                text = "%s t%s(%s)->%s.t%s%s"%(dp,m,byte,shu,t,cond)
                                #print text
                                selranges = QTableWidgetSelectionRange(row, column, row, column)
                                self.inittablewidget.setRangeSelected(selranges, True)
                                self.inittablewidget.setItem(row, column,QTableWidgetItem(text))
                                self.inittablewidget.dataParser(row, column)
                                self.assertEqual(self.inittablewidget.item(row, column).background(),self.inittablewidget.defaultBackgroundColor)
                                self.assertEqual(self.inittablewidget.database.searchMcc(self.inittablewidget.mmpulite.result), "4")


    def testDataIalu_7(self):
        self.main.newFile()
        row = random.randint(0,1999)
        column = random.randint(0,19)
        biulist = ["biu0","biu1","biu2"]
        bytelist = ["b","u,b","h","u,h"]
        dplist = ["expd"]
        for dp in dplist:
            for m in xrange(0,4):
                for byte in bytelist:
                    for biu in biulist:
                        for cond in condlist:
                            text = "%s t%s(%s)->%s%s"%(dp,m,byte,biu,cond)
                            #print text
                            selranges = QTableWidgetSelectionRange(row, column, row, column)
                            self.inittablewidget.setRangeSelected(selranges, True)
                            self.inittablewidget.setItem(row, column,QTableWidgetItem(text))
                            self.inittablewidget.dataParser(row, column)
                            self.assertEqual(self.inittablewidget.item(row, column).background(),self.inittablewidget.defaultBackgroundColor)
                            self.assertEqual(self.inittablewidget.database.searchMcc(self.inittablewidget.mmpulite.result), "4-5")

    def testDataIalu_8(self):
        self.main.newFile()
        row = random.randint(0,1999)
        column = random.randint(0,19)
        bytelist = ["b","u,b","h","u,h"]
        dplist = ["expd"]
        for dp in dplist:
            for m in xrange(0,4):
                for byte in bytelist:
                    for t in xrange(0,127):
                        for cond in condlist:
                            text = "%s t%s(%s)->m[%s]%s"%(dp,m,byte,t,cond)
                            #print text
                            selranges = QTableWidgetSelectionRange(row, column, row, column)
                            self.inittablewidget.setRangeSelected(selranges, True)
                            self.inittablewidget.setItem(row, column,QTableWidgetItem(text))
                            self.inittablewidget.dataParser(row, column)
                            self.assertEqual(self.inittablewidget.item(row, column).background(),self.inittablewidget.defaultBackgroundColor)
                            self.assertEqual(self.inittablewidget.database.searchMcc(self.inittablewidget.mmpulite.result), "4-5")


    def testDataIalu_9(self):
        self.main.newFile()
        row = random.randint(0,1999)
        column = random.randint(0,19)
        bytelist = ["b","u,b","h","u,h"]
        macclist = ["ialu","imac","falu"]
        dplist = ["expd"]
        for dp in dplist:
            for m in xrange(0,4):
                for byte in bytelist:
                    for macc in macclist:
                        for t in xrange(0,4):
                            for cond in condlist:
                                text = "%s t%s(%s)->%s.t%s%s"%(dp,m,byte,macc,t,cond)
                                #print text
                                selranges = QTableWidgetSelectionRange(row, column, row, column)
                                self.inittablewidget.setRangeSelected(selranges, True)
                                self.inittablewidget.setItem(row, column,QTableWidgetItem(text))
                                self.inittablewidget.dataParser(row, column)
                                self.assertEqual(self.inittablewidget.item(row, column).background(),self.inittablewidget.defaultBackgroundColor)
                                self.assertEqual(self.inittablewidget.database.searchMcc(self.inittablewidget.mmpulite.result), "3-4")


    def testDataIalu_10(self):
        self.main.newFile()
        row = random.randint(0,1999)
        column = random.randint(0,19)
        shulist = ["shu0","shu1"]
        bytelist = ["b","u,b","h","u,h"]
        dplist = ["expd"]
        for dp in dplist:
            for m in xrange(0,4):
                for byte in bytelist:
                    for shu in shulist:
                        for t in xrange(0,4):
                            for cond in condlist:
                                text = "%s t%s(%s)->%s.t%s%s"%(dp,m,byte,shu,t,cond)
                                #print text
                                selranges = QTableWidgetSelectionRange(row, column, row, column)
                                self.inittablewidget.setRangeSelected(selranges, True)
                                self.inittablewidget.setItem(row, column,QTableWidgetItem(text))
                                self.inittablewidget.dataParser(row, column)
                                self.assertEqual(self.inittablewidget.item(row, column).background(),self.inittablewidget.defaultBackgroundColor)
                                self.assertEqual(self.inittablewidget.database.searchMcc(self.inittablewidget.mmpulite.result), "4-5")


    def testDataIalu_11(self):
        self.main.newFile()
        row = random.randint(0,1999)
        column = random.randint(0,19)
        biulist = ["biu0","biu1","biu2"]
        bytelist = ["","(u)","(h)","(u,h)"]
        dplist = ["cprs"]
        for dp in dplist:
            for m in xrange(0,4):
                for n in xrange(0,4):
                    for byte in bytelist:
                        for biu in biulist:
                            for cond in condlist:
                                text = "%s (t%s,t%s)%s->%s%s"%(dp,m,n,byte,biu,cond)
                                #print text
                                selranges = QTableWidgetSelectionRange(row, column, row, column)
                                self.inittablewidget.setRangeSelected(selranges, True)
                                self.inittablewidget.setItem(row, column,QTableWidgetItem(text))
                                self.inittablewidget.dataParser(row, column)
                                self.assertEqual(self.inittablewidget.item(row, column).background(),self.inittablewidget.defaultBackgroundColor)
                                self.assertEqual(self.inittablewidget.database.searchMcc(self.inittablewidget.mmpulite.result), "4")

    def testDataIalu_12(self):
        self.main.newFile()
        row = random.randint(0,1999)
        column = random.randint(0,19)
        bytelist = ["","(u)","(h)","(u,h)"]
        dplist = ["cprs"]
        for dp in dplist:
            for m in xrange(0,4):
                for n in xrange(0,4):
                    for byte in bytelist:
                        for t in xrange(0,127):
                            for cond in condlist:
                                text = "%s (t%s,t%s)%s->m[%s]%s"%(dp,m,n,byte,t,cond)
                                #print text
                                selranges = QTableWidgetSelectionRange(row, column, row, column)
                                self.inittablewidget.setRangeSelected(selranges, True)
                                self.inittablewidget.setItem(row, column,QTableWidgetItem(text))
                                self.inittablewidget.dataParser(row, column)
                                self.assertEqual(self.inittablewidget.item(row, column).background(),self.inittablewidget.defaultBackgroundColor)
                                self.assertEqual(self.inittablewidget.database.searchMcc(self.inittablewidget.mmpulite.result), "4")


    def testDataIalu_13(self):
        self.main.newFile()
        row = random.randint(0,1999)
        column = random.randint(0,19)
        bytelist = ["","(u)","(h)","(u,h)"]
        macclist = ["ialu","imac","falu"]
        dplist = ["cprs"]
        for dp in dplist:
            for m in xrange(0,4):
                for n in xrange(0,4):
                    for byte in bytelist:
                        for macc in macclist:
                            for t in xrange(0,4):
                                for cond in condlist:
                                    text = "%s (t%s,t%s)%s->%s.t%s%s"%(dp,m,n,byte,macc,t,cond)
                                    #print text
                                    selranges = QTableWidgetSelectionRange(row, column, row, column)
                                    self.inittablewidget.setRangeSelected(selranges, True)
                                    self.inittablewidget.setItem(row, column,QTableWidgetItem(text))
                                    self.inittablewidget.dataParser(row, column)
                                    self.assertEqual(self.inittablewidget.item(row, column).background(),self.inittablewidget.defaultBackgroundColor)
                                    self.assertEqual(self.inittablewidget.database.searchMcc(self.inittablewidget.mmpulite.result), "3")

    def testDataIalu_14(self):
        self.main.newFile()
        row = random.randint(0,1999)
        column = random.randint(0,19)
        shulist = ["shu0","shu1"]
        bytelist = ["","(u)","(h)","(u,h)"]
        dplist = ["cprs"]
        for dp in dplist:
            for m in xrange(0,4):
                for n in xrange(0,4):
                    for byte in bytelist:
                        for shu in shulist:
                            for t in xrange(0,4):
                                for cond in condlist:
                                    text = "%s (t%s,t%s)%s->%s.t%s%s"%(dp,m,n,byte,shu,t,cond)
                                    #print text
                                    selranges = QTableWidgetSelectionRange(row, column, row, column)
                                    self.inittablewidget.setRangeSelected(selranges, True)
                                    self.inittablewidget.setItem(row, column,QTableWidgetItem(text))
                                    self.inittablewidget.dataParser(row, column)
                                    self.assertEqual(self.inittablewidget.item(row, column).background(),self.inittablewidget.defaultBackgroundColor)
                                    self.assertEqual(self.inittablewidget.database.searchMcc(self.inittablewidget.mmpulite.result), "4")

suite = unittest.TestLoader().loadTestsFromTestCase(mytest)
unittest.TextTestRunner(verbosity=2).run(suite)
