# -*- coding: utf-8 -*-   
import sys
from PyQt4.QtGui import QTableWidgetItem, QBrush, QColor
from PyQt4.QtCore import Qt, pyqtSignal, pyqtSlot, SIGNAL, QStringList, QString
from view.MicrocodeTableWidget.InitTableWidget import InitTableWidget
from view.Utils import warning
from fileinput import filename
sys.path.append("../..")
from data.RectInfo import RectInfo
from data.MMPULite import MMPULite
import re
from subprocess import Popen, PIPE

class MicrocodeTableWidget(InitTableWidget):  
    searchTreeSignal = pyqtSignal(int, int, str)
    itemRegStateSignal = pyqtSignal(list, list)
    def __init__(self, register, database, parent = None):  
        super(MicrocodeTableWidget, self).__init__(parent)   

        self.register = register
        self.database = database
        self.connect(self, SIGNAL("currentCellChanged(int, int, int, int)"), self.currentCellChangedSlot)
        self.connect(self.horizontalScrollBar(), SIGNAL("valueChanged(int)"), self.horizontalScrollBarChangedSlot)
        self.connect(self.verticalScrollBar(), SIGNAL("valueChanged(int)"), self.verticalScrollBarChangedSlot)
        #record the previous point row
        self.previousPointRow = -1
        #MMPULite parser
        self.mmpulite = MMPULite()
        self.errorColor = QColor(255, 99, 71)

    @pyqtSlot(int, int, int, int)   
    def currentCellChangedSlot(self, currentRow, currentColumn, previousRow, previousColumn):      
        self.dataParser(previousRow, previousColumn)
        self.floatDialogCloseSlot()
        self.CurrentRow = previousRow
        self.CurrentColumn = previousColumn
        #show reg info
        regList = []
        marginList = [0, 0, 0, 0]
        if currentRow < len(self.array):
            text = self.array[currentRow][currentColumn]
            textList = text.split(".")
            regList = textList[1].split(",")
            if len(regList) > 0:
                del regList[-1]
            rectList = self.loopBodyList[currentColumn]
            for info in rectList:
                if info.startRow <= currentRow and info.endRow >= currentRow:
                    marginList[info.reg] = info.margin 
        #self.itemRegStateSignal.emit(regList, marginList)   
        #show code input row, for instruction latency
        
        if self.previousPointRow != -1:
            for i in self.previousPointRow:
                self.earserWholeRowColor(i)   
        item = self.item(currentRow, currentColumn)
        if item != None:
            if item.text() == "":
                return  
            if item.whatsThis() == "" or item.whatsThis() == "-1":
                return
            out = item.whatsThis().split("-")
            self.previousPointRow = []   
            for i in out:
                rowColor = []
                outRow = currentRow + int(i)        
                color = self.getRowBackground(outRow)
                #self.setWholeRowColor(outRow, Qt.blue) 
                rowColor.append(outRow)
                rowColor.append(color)
                self.previousPointRow.append(rowColor)
        else:
            self.previousPointRow = -1 

    @pyqtSlot(int)
    def horizontalScrollBarChangedSlot(self, i):
        self.floatDialogCloseSlot()

    @pyqtSlot(int)
    def verticalScrollBarChangedSlot(self, i):
        self.floatDialogCloseSlot()
      
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Down:
            if self.floatDialog != 0:
                if self.floatDialog.isVisible() == True:
                    if self.floatDialogFocus == 0:
                        item = self.floatDialog.item(0)
                        if item != None:
                            self.floatDialog.setCurrentItem(item)
                            self.floatDialogFocus = 1
                    elif self.floatDialogFocus == 1:
                        row = self.floatDialog.currentRow()
                        num = self.floatDialog.count()
                        if row + 1 < num:
                            self.floatDialog.setCurrentRow(row + 1)    
            #change item position
            if self.currentColumn() >= 0 and self.currentRow() >= 0 and self.currentRow() < (self.rowCount() - 1):
                self.setCurrentCell(self.currentRow() + 1, self.currentColumn())
        elif event.key() == Qt.Key_Up:      
            if self.floatDialogFocus == 1:
                row = self.floatDialog.currentRow()
                if row > 0:
                    self.floatDialog.setCurrentRow(row - 1)
            #change item position
            if self.currentColumn() >= 0 and self.currentRow() >= 0 and self.currentRow() > 0:
                self.setCurrentCell(self.currentRow() - 1, self.currentColumn())
        elif event.key() == Qt.Key_Return:
            if self.floatDialog != 0:
                item = self.floatDialog.currentItem()
                if item == None:
                    return
                text = item.text()
                column = self.currentColumn()
                row = self.currentRow()
                item = QTableWidgetItem(text)           
                self.setItem(row, column, item)
                self.floatDialogCloseSlot()
            #change item position
            if self.currentColumn() >= 0 and self.currentRow() >= 0 and self.currentRow() < (self.rowCount() - 1):
                self.setCurrentCell(self.currentRow() + 1, self.currentColumn())
        elif event.key() == Qt.Key_Left:
            #change item position
            if self.currentColumn() >= 0 and self.currentRow() >= 0 and self.currentColumn() > 0:
                self.setCurrentCell(self.currentRow(), self.currentColumn() - 1)            
        elif event.key() == Qt.Key_Right:
            #change item position
            if self.currentColumn() >= 0 and self.currentRow() >= 0 and self.currentColumn() < (self.columnCount() - 1):
                self.setCurrentCell(self.currentRow(), self.currentColumn() + 1)
        elif event.key() == Qt.Key_Tab:
            #change item position
            if self.currentColumn() >= 0 and self.currentRow() >= 0 and self.currentColumn() < (self.columnCount() - 1):
                self.setCurrentCell(self.currentRow(), self.currentColumn() + 1)
                
        if event.key() < 0x20 or event.key() > 0xff:
            if event.key() != Qt.Key_Backspace:
                return
        column = self.currentColumn()
        row = self.currentRow()
        item = self.item(row, column)
        if item != None:
            string = item.text()
        else:
            string = ""
        if event.key() != Qt.Key_Backspace:
            if row == self.CurrentRow and column == self.CurrentColumn:
                self.setItem(row, column, QTableWidgetItem(string + event.text()))
            else:
                self.setItem(row, column, QTableWidgetItem(event.text()))
        
        else:
            if row == self.CurrentRow and column == self.CurrentColumn:
                if len(string) > 1:
                    string = string[0:-1]
                else:
                    string = ""
                self.setItem(row, column, QTableWidgetItem(string))
            else:
                string = ""
                self.setItem(row, column, QTableWidgetItem(string))
           
        self.CurrentRow = row
        self.CurrentColumn = column
        text = self.item(row, column).text()
        #dissable auto-fill
        #if len(text) > 1:
        #    self.searchTreeSignal.emit(row, column, text)

    def setRectInfo(self, reg):
        rectInfo = RectInfo()
        rectInfo.reg = reg

        selRange = self.selectedRange()
        self.currentRowNum = selRange.rowCount()
        self.currentColumnNum = selRange.columnCount()
        if self.currentColumnNum == 0:
            return -1
        if self.currentColumnNum > 1:
            return 0
        self.currentTopRow = selRange.topRow()
        self.currentLeftColumn = selRange.leftColumn()  
        rectInfo.startRow = self.currentTopRow
        rectInfo.endRow = self.currentTopRow + self.currentRowNum - 1
        rectInfo.column = self.currentLeftColumn
        #check selected cells
        columnList = self.loopBodyList[self.currentLeftColumn]
        num = len(columnList)
        for i in range(num):
            cmpInfo = columnList[i]
            if cmpInfo.startRow < rectInfo.startRow and cmpInfo.endRow < rectInfo.endRow and rectInfo.startRow < cmpInfo.endRow:
                return -2
        return rectInfo 

    def setItemInfo(self, info) :
        #update the items reg and frame info
        for i in xrange(info.startRow, info.endRow + 1):  
            if info.startRow == info.endRow:
                text = self.array[info.startRow][info.column]
                textList = text.split(".")
                num = len(textList)
                for i in xrange(num - 1):
                    regText = textList[i]
                    regText = "%s%s,"%(regText, str(info.reg))
                    textList[i] = regText                             
                text = "%s.%s.%s.%s.%s"%(textList[0], textList[1], textList[2], textList[3], textList[4])  
                self.array[info.startRow][info.column] = text     
                break
            if i == info.startRow:
                text = self.array[i][info.column]
                textList = text.split(".")
                #up, right, left
                for j in [0, 1, 3]:
                    regText = textList[j]
                    regText = "%s%s,"%(regText,str(info.reg))
                    textList[j] = regText 
                text = "%s.%s.%s.%s.%s"%(textList[0], textList[1], textList[2], textList[3], textList[4])  
                self.array[i][info.column] = text
            elif i == info.endRow:
                text = self.array[i][info.column]
                textList = text.split(".")
                #right, bottom, left
                for j in [1, 2, 3]:
                    regText = textList[j]
                    regText = "%s%s,"%(regText,str(info.reg))
                    textList[j] = regText 
                text = "%s.%s.%s.%s.%s"%(textList[0], textList[1], textList[2], textList[3], textList[4])  
                self.array[i][info.column] = text
            else:
                text = self.array[i][info.column]
                textList = text.split(".")
                #right, left
                for j in [1, 3]:
                    regText = textList[j]
                    regText = "%s%s,"%(regText,str(info.reg))
                    textList[j] = regText 
                text = "%s.%s.%s.%s.%s"%(textList[0], textList[1], textList[2], textList[3], textList[4])  
                self.array[i][info.column] = text                    
        
    def paintRect(self, reg, text):
        rectInfo = self.setRectInfo(reg)
        if rectInfo == 0 or rectInfo == -1 or rectInfo == -2:
            return rectInfo
        rectInfo.margin = int(text)
        if rectInfo.endRow > self.loopEndRow:
            for i in xrange(self.loopEndRow, rectInfo.endRow):
                self.array.append(["...."]*(self.ColumnCount))
            self.loopEndRow = rectInfo.endRow
        #add loopBodyList
        self.loopBodyList[rectInfo.column].append(rectInfo)
        self.setItemInfo(rectInfo) 
        self.viewport().update() 
        return 1

    def eraserRect(self, reg):
        selRange = self.selectedRange()
        self.currentTopRow = selRange.topRow()
        self.currentLeftColumn = selRange.leftColumn()
        columnList = self.loopBodyList[self.currentLeftColumn]
        num = len(columnList)
        if num == 0:
            return              
        for i in xrange(num, 0, -1):
           rectInfo = columnList[i - 1]
           if rectInfo.reg == reg and rectInfo.startRow <= self.currentTopRow and rectInfo.endRow >= self.currentTopRow:
                columnList.remove(rectInfo)        
                #remove item reg info and frame                
                for i in xrange(rectInfo.startRow, rectInfo.endRow + 1):
                    if rectInfo.startRow == rectInfo.endRow:
                        text = self.array[i][self.currentLeftColumn]
                        textList = text.split(".")
                        num = len(textList)
                        for j in xrange(num - 1):
                            regText = textList[j]
                            regList = regText.split(",")
                            regNum = len(regList)
                            for k in xrange(regNum - 1):
                                if regList[k] == str(reg):
                                    regList.remove(str(reg))
                                    break
                            regNum = len(regList)
                            regText = ""
                            for k in xrange(regNum - 1):
                                regText = "%s%s,"%(regText, regList[k])
                            textList[j] = regText                             
                        text = "%s.%s.%s.%s.%s"%(textList[0], textList[1], textList[2], textList[3], textList[4])  
                        self.array[rectInfo.startRow][self.currentLeftColumn] = text 
                        break    
                    if i == rectInfo.startRow:
                        text = self.array[i][self.currentLeftColumn]
                        textList = text.split(".")
                        #up, right, left
                        for j in [0, 1, 3]:
                            regText = textList[j]
                            regList = regText.split(",")
                            regNum = len(regList)
                            for k in xrange(regNum - 1):
                                if regList[k] == str(reg):
                                    regList.remove(str(reg))
                                    break
                            regNum = len(regList)
                            regText = ""
                            for k in xrange(regNum - 1):
                                regText = "%s%s,"%(regText, regList[k])
                            textList[j] = regText                                             
                        text = "%s.%s.%s.%s.%s"%(textList[0], textList[1], textList[2], textList[3], textList[4]) 
                        self.array[i][self.currentLeftColumn] = text
                    elif i == rectInfo.endRow:
                        text = self.array[i][self.currentLeftColumn]
                        textList = text.split(".")
                        #right, bottom, left
                        for j in [1, 2, 3]:
                            regText = textList[j]
                            regList = regText.split(",")
                            regNum = len(regList)
                            for k in xrange(regNum - 1):
                                if regList[k] == str(reg):
                                    regList.remove(str(reg))
                                    break
                            regNum = len(regList)
                            regText = ""
                            for k in xrange(regNum - 1):
                                regText = "%s%s,"%(regText, regList[k])
                            textList[j] = regText                                             
                        text = "%s.%s.%s.%s.%s"%(textList[0], textList[1], textList[2], textList[3], textList[4])  
                        self.array[i][self.currentLeftColumn] = text
                    else:
                        text = self.array[i][self.currentLeftColumn]
                        textList = text.split(".")
                        #right, left
                        for j in [1, 3]:
                            regText = textList[j]
                            regList = regText.split(",")
                            regNum = len(regList)
                            for k in xrange(regNum - 1):
                                if regList[k] == str(reg):
                                    regList.remove(str(reg))
                                    break
                            regNum = len(regList)
                            regText = ""
                            for k in xrange(regNum - 1):
                                regText = "%s%s,"%(regText, regList[k])
                            textList[j] = regText                                             
                        text = "%s.%s.%s.%s.%s"%(textList[0], textList[1], textList[2], textList[3], textList[4]) 
                        self.array[i][self.currentLeftColumn] = text 
        self.viewport().update()                              

    def getRowBackground(self, row):
        rowColor = []
        count = self.getColumnCount()
        for i in xrange(count):
            item = self.item(row, i)
            if item == None:
                self.setItem(row, i, QTableWidgetItem(""))
                item = self.item(row, i)
            rowColor.append(item.background())
        return rowColor

    def setWholeRowColor(self, row, color):
        count = self.getColumnCount()
        for i in xrange(0, count):
            item = self.item(row, i)
            if item == None:
                item = QTableWidgetItem("")
                self.setItem(row, i, item)
            item.setBackground(QBrush(color))
        
    def earserWholeRowColor(self, rowColor):
        count = self.getColumnCount()
        row = rowColor[0]
        color = rowColor[1]
        for i in xrange(0, count):
            item = self.item(row, i)
            if item == None:
                item = QTableWidgetItem("")
                self.setItem(row, i, item)
            item.setBackground(color[i])    

    def searchLPStart(self, rectList, row):
        cmpList = []
        n = 1
        for info in rectList:
            info.num = n
            n += 1
            if info.startRow == row:
                if cmpList != []:
                    tmp = cmpList[-1]
                    if tmp.endRow < info.endRow:
                        cmpList.insert(0, info)
                    else:
                        cmpList.append(info)
                else:
                    cmpList.append(info)
        return cmpList

    def searchLPEnd(self, rectList, row):
        cmpList = []
        for info in rectList:
            if info.endRow == row and info.startRow != info.endRow:
                if cmpList != []:
                    tmp = cmpList[-1]
                    if tmp.startRow <= info.startRow:
                        cmpList.insert(0, info)
                    else:
                        cmpList.append(info)
                else:
                    cmpList.append(info)
        return cmpList

    def saveFile(self, fileName):
        fp = open(fileName, "w")
        #update self.SlotRecordTable, effective row/column count
        startrow = self.MaxRowNum #init with big number
        effectivecolumncount = -1
        effectiverowcount = -1
        for column in xrange(self.ColumnCount):
            top = -1
            bottom = -1
            for row in xrange(self.RowCount):
                item = self.item(row, column)
                if item != None and item.text() != "":
                    effectivecolumncount = max(effectivecolumncount, column)
                    effectiverowcount = max(effectiverowcount, row)
                    if top == -1:
                        top = row
                    bottom = max(bottom, row)
            if top != -1:
                self.SlotRecordTable[column][0] = top
                self.SlotRecordTable[column][1] = bottom
                startrow = min(startrow, top)
            else:
                self.SlotRecordTable[column][0] = -1
                self.SlotRecordTable[column][1] = -1
        self.InsStartRow = startrow
        self.EffectiveColumnCount = effectivecolumncount
        self.EffectiveRowCount = effectiverowcount

        #generate FSM style code
        if self.FSMCodeSelectEnable == True:
            for column in xrange(self.ColumnCount):
                if self.SlotRecordTable[column][0] == 1:
                    lines = []
                    headeritem = self.horizontalHeaderItem(column)
                    headertext = str(headeritem.text())
                    line = ".hmacro hm_%s\n" % (headertext)
                    lines.append(line)
                    for row in xrange(self.SlotRecordTable[column][1] + 1):                   
                        item = self.item(row, column)
                        if item == None or item.text() == "":
                            line = "NOP;"
                        else:
                            line = item.text()
                            if line[-1] != ';':
                                line += ';'
                        line += '\n'
                        lines.append(line)
                    lines.append(".endhmacro\n\n")
                    fp.writelines(lines)
        #generate ordinary VLIW style code
        else:
            lines = [] 
            for row in xrange(self.InsStartRow, self.EffectiveRowCount + 1):
                line = ""
                for column in xrange(self.EffectiveColumnCount + 1):
                    instext = ""
                    if self.SlotRecordTable[column][0] == -1: #skip ineffective column
                        continue
                    
                    startdistance = self.SlotRecordTable[column][0] - self.InsStartRow
                    item = self.item(row + startdistance - 1, column)
                    if row == self.InsStartRow:
                        if startdistance == 0:
                            instext += ""#the 1st instruction, nop in parallel with wait instructions
                        else:
                            instext = "%s.wait %d(mode0)" % (self.horizontalHeaderItem(column).text(), startdistance)
                    else:
                        if item != None and item.text() != "":
                            instext = item.text()
                    if instext != "":
                        if line == "":
                            line += instext
                        else:
                            line += " || " + instext                   
                        if line[-1] == ';' and len(line) > 1:
                            line = line[0:-1]                              
                if line == "":
                    line = "NOP"
                line += ";\n"
                lines.append(line)        
            fp.writelines(lines)
            
        fp.close()
        
        '''
        usage of calling command line
        '''               
        arg1 = 'ls'
        arg2 = '-a'
        popen = Popen([arg1, arg2], stdout=PIPE, stderr=PIPE)
        output, err = popen.communicate()
        rcode = popen.returncode
        
        
    def openFile(self, fileName): 
        headerPattern = re.compile("\.hmacro ([a-zA-Z]+[0-9]+)")
        endPattern = re.compile("\.endhmacro")
        startLPPattern = re.compile("LPTO \((\d+)f \) @ \((\w+)( - )?(\d*)\)")
        oneLPPattern = re.compile("Repeat @ \((\w+)( - )?(\d*)\)")
        endLPPattern = re.compile("(\d+):")
        rowPattern = re.compile("(.+);")

        fp = open(fileName, "r")
        stringList = fp.readlines()   
        column = -1
        row = 0
        previous = 0
        for string in stringList[0 : -3]:
            if headerPattern.search(string) != None:        
                record = headerPattern.search(string)
                column += 1
                if column >= self.ColumnCount:
                    self.ColumnCount = column + 1
                    self.setColumnCount(self.ColumnCount)
                    self.loopBodyList.append([])
                    num = len(self.array)
                    for i in xrange(num):
                        data = self.array[i]
                        data.append("....")
                row = 0
                self.setHorizontalHeaderItem(column, QTableWidgetItem(record.group(1)))
            elif startLPPattern.search(string) != None:                     
                record = string.split(" || ")
                if len(record) == 1 or startLPPattern.match(record[0]) != None:
                    self.setItem(row, column, QTableWidgetItem(""))
                    self.dataParser(row, column)
                    row += 1
                    if row > self.RowCount:
                        self.RowCount = row
                        self.setRowCount(row)
                if len(record) > 1:
                    for lpto in record:
                        if startLPPattern.match(lpto) != None:
                            r = startLPPattern.match(lpto)        
                            info = RectInfo()
                            info.startRow = row
                            info.num = int(r.group(1))
                            info.reg = self.register.index(r.group(2))
                            if r.group(3) != None:
                                info.margin = int(r.group(4))
                            else:
                                info.margin = 0
                            info.column = column
                            item = QTableWidgetItem("")
                            self.setItem(row, column, item)
                            self.dataParser(row, column)
                            self.loopBodyList[column].append(info)
                        else:
                            if lpto == "NOP":
                                text = ""
                            else:
                                text = record[0]
                            self.setItem(row, column, QTableWidgetItem(text))
                            self.dataParser(row, column)
                            row += 1
                            if row > self.RowCount:
                                self.RowCount = row
                                self.setRowCount(row)
                else:
                    record = startLPPattern.match(string)        
                    info = RectInfo()
                    info.startRow = row
                    info.num = int(record.group(1))
                    info.reg = self.register.index(record.group(2))
                    if record.group(3) != None:
                        info.margin = int(record.group(4))
                    else:
                        info.margin = 0
                    info.column = column
                    item = QTableWidgetItem("")
                    self.setItem(row, column, item)
                    self.dataParser(row, column)
                    self.loopBodyList[column].append(info)
            elif oneLPPattern.search(string) != None:
                record = string.split(" || ")
                if record[0] == "NOP":
                    text = ""
                else:
                    text = record[0]
                self.setItem(row, column, QTableWidgetItem(text))
                self.dataParser(row, column)
                if row > self.RowCount:
                    self.RowCount = row
                    self.setRowCount(row)
                for lpto in record[1 : ]:
                    record = oneLPPattern.match(lpto)        
                    info = RectInfo()
                    info.startRow = row
                    info.endRow = row
                    info.num = 1
                    info.reg = self.register.index(record.group(1))
                    if record.group(2) != None:
                        info.margin = int(record.group(3))
                    else:
                        info.margin = 0
                    info.column = column
                    self.loopBodyList[column].append(info)
                    if info.endRow > self.loopEndRow:
                        for i in xrange(self.loopEndRow, info.endRow):
                            self.array.append(["...."]*(self.ColumnCount))
                            self.loopEndRow = info.endRow
                    self.setItemInfo(info)
                    row += 1
            elif endLPPattern.search(string) != None:        
                record = endLPPattern.search(string)
                columnList = self.loopBodyList[column]
                for info in columnList:
                    if info.num == int(record.group(1)):
                        info.endRow = (row - 1)
                        if info.endRow > self.loopEndRow:
                            for i in xrange(self.loopEndRow, info.endRow):
                                self.array.append(["...."]*(self.ColumnCount))
                                self.loopEndRow = info.endRow
                        self.setItemInfo(info)
                        break
            elif rowPattern.search(string) != None:
                record = rowPattern.search(string)
                text = record.group(1)
                if text == "NOP":
                    text = ""
                else:
                    if row > self.loopEndRow:
                        for i in xrange(self.loopEndRow, row):
                            self.array.append(["...."]*(self.ColumnCount))
                            self.loopEndRow = row
                self.setItem(row, column, QTableWidgetItem(text))
                self.dataParser(row, column)
                row += 1
                if row > self.RowCount:
                    self.RowCount = row
                    self.setRowCount(row)
            previous = string   
                 
        fp.close()

