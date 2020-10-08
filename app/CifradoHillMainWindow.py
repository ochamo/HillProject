from PyQt5 import QtWidgets, uic
import sys

class CifradoHillMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(CifradoHillMainWindow, self).__init__()
        uic.loadUi('resources/ui/MainWindow.ui', self)
        self.setupClickListeners()
        self.show()
    
    def setupClickListeners(self):
        self.openEncripteryMatrix = self.findChild(QtWidgets.QPushButton, "openEncrypterMatrix")
        self.openEncripteryMatrix.clicked.connect(self.openFileExplorer)

    def openFileExplorer(self):
        QtWidgets.QFileDialog.getOpenFileName(self)

