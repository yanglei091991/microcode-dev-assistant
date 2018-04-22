from PyQt4.QtGui import QDialog, QRadioButton, QLabel, QPushButton, QColor, QVBoxLayout, QHBoxLayout, QGridLayout, QPainter, QBrush
from PyQt4.QtCore import Qt, SIGNAL, pyqtSlot, pyqtSignal

class ColorDialog(QDialog):
    OKColorSignal = pyqtSignal(QColor)
    OKIndexSignal = pyqtSignal(int)
    def __init__(self, color, parent = None):
        super(ColorDialog, self).__init__(parent)
        
	self.color = color
	self.setWindowTitle("Color select")
	self.greyRadio = QRadioButton()
	self.greyRadio.setFixedSize(25, 25)
	self.greyRadio.setChecked(True)
	self.greyRadio.clicked.connect(self.greySlot)
	self.greyLabel = QLabel()
	self.blueRadio = QRadioButton()
	self.blueRadio.setFixedSize(25, 25)
	self.blueRadio.clicked.connect(self.blueSlot)
	self.blueLabel = QLabel()
	self.yellowRadio = QRadioButton()
	self.yellowRadio.setFixedSize(25, 25)
	self.yellowRadio.clicked.connect(self.yellowSlot)
	self.yellowLabel = QLabel()
	self.pinkRadio = QRadioButton()
	self.pinkRadio.setFixedSize(25, 25)
	self.pinkRadio.clicked.connect(self.pinkSlot)
	self.pinkLabel = QLabel()
	self.purpleRadio = QRadioButton()
	self.purpleRadio.setFixedSize(25, 25)
	self.purpleRadio.clicked.connect(self.purpleSlot)
	self.purpleLabel = QLabel()
	self.defaultRadio = QRadioButton()
	self.defaultRadio.setFixedSize(25, 25)
	self.defaultRadio.clicked.connect(self.defaultSlot)
	self.defaultLabel = QLabel("No Fill")
	radioLay = QGridLayout()
	radioLay.setMargin(0)
	radioLay.addWidget(self.greyRadio, 0, 0)
	radioLay.addWidget(self.greyLabel, 0, 1)
	radioLay.addWidget(self.blueRadio, 1, 0)
	radioLay.addWidget(self.blueLabel, 1, 1)
	radioLay.addWidget(self.yellowRadio, 2, 0)
	radioLay.addWidget(self.yellowLabel, 2, 1)
	radioLay.addWidget(self.pinkRadio, 3, 0)
	radioLay.addWidget(self.pinkLabel, 3, 1)
	radioLay.addWidget(self.purpleRadio, 4, 0)
	radioLay.addWidget(self.purpleLabel, 4, 1)
	radioLay.addWidget(self.defaultRadio, 5, 0)
	radioLay.addWidget(self.defaultLabel, 5, 1)
	
	self.OKButton = QPushButton("OK")
	self.cancelButton = QPushButton("Cancel")
	self.OKButton.clicked.connect(self.OKSlot)
	self.cancelButton.clicked.connect(self.cancelSlot)
	buttonLay = QHBoxLayout()
	buttonLay.addWidget(self.OKButton)
	buttonLay.addWidget(self.cancelButton)
	
	mainLay = QVBoxLayout()
	mainLay.addLayout(radioLay)
	mainLay.addLayout(buttonLay)
	self.setLayout(mainLay)
	
	self.index = 0

    @pyqtSlot()
    def OKSlot(self):
	if self.index == 5:
	    self.OKIndexSignal.emit(self.index)
	else:
	    self.OKColorSignal.emit(self.color[self.index])
	self.close()
    
    @pyqtSlot()
    def cancelSlot(self):
	self.close()

    @pyqtSlot()
    def greySlot(self):
	self.index = 0

    @pyqtSlot()
    def blueSlot(self):
	self.index = 1
	
    @pyqtSlot()
    def yellowSlot(self):
	self.index = 2
	
    @pyqtSlot()
    def pinkSlot(self):
	self.index = 3

    @pyqtSlot()
    def purpleSlot(self):
	self.index = 4
	
    @pyqtSlot()
    def defaultSlot(self):
	self.index = 5

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        
        rect = self.greyLabel.geometry()
        greyGradient = self.color[0]
        painter.setBrush(QBrush(greyGradient)) 
        painter.drawRect(rect)

        rect = self.blueLabel.geometry()
        blueGradient = self.color[1]
        painter.setBrush(QBrush(blueGradient)) 
        painter.drawRect(rect)

        rect = self.yellowLabel.geometry()
        yellowGradient = self.color[2]
        painter.setBrush(QBrush(yellowGradient)) 
        painter.drawRect(rect)
    
        rect = self.pinkLabel.geometry()
        pinkGradient = self.color[3]
        painter.setBrush(QBrush(pinkGradient)) 
        painter.drawRect(rect)
        
        rect = self.purpleLabel.geometry()
        purpleGradient = self.color[4]
        painter.setBrush(QBrush(purpleGradient)) 
        painter.drawRect(rect)
        
        painter.end()
   