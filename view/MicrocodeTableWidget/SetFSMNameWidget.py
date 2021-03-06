# -*- coding: utf-8 -*-   
from PyQt4.QtGui import QLabel, QDialog, QRegExpValidator, QPushButton, QHBoxLayout, QVBoxLayout, QLineEdit
from PyQt4.QtCore import pyqtSignal, pyqtSlot, SIGNAL, Qt, QRegExp
from view.Utils import warning

class SetFSMNameWidget(QDialog):  
    setFSMNameSignal = pyqtSignal(int, str)
    def __init__(self, column, parent = None):  
        super(SetFSMNameWidget, self).__init__(parent)   

        self.setWindowTitle("Set FSM Name")
        self.tip_label = QLabel("Set a FSM name, staring with letter of '_'")
        self.lineEdit = QLineEdit()
        regx = QRegExp("[_a-zA-Z]+[0-9]+$")
        validator = QRegExpValidator(regx, self.lineEdit)
        self.lineEdit.setValidator(validator)

        self.OKButton = QPushButton("OK")
        self.cancelButton = QPushButton("Cancel")	

        lay = QHBoxLayout()
        lay.addWidget(self.OKButton)
        lay.addWidget(self.cancelButton)
        mainLay = QVBoxLayout()
        mainLay.addWidget(self.tip_label)
        mainLay.addWidget(self.lineEdit)
        mainLay.addLayout(lay)

        self.setLayout(mainLay)
        self.column = column

        self.connect(self.OKButton, SIGNAL("clicked()"), self.OKButtonSlot)
        self.connect(self.cancelButton, SIGNAL("clicked()"), self.cancelButtonSlot)

    @pyqtSlot()
    def OKButtonSlot(self):
        text = self.lineEdit.text()
        if text != "":
            self.close()
            self.setFSMNameSignal.emit(self.column, text)
        else:
            warning("Please set FSM name")

    @pyqtSlot()	
    def cancelButtonSlot(self):
        self.close()

