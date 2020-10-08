from PyQt5 import QtWidgets

from .CifradoHillMainWindow import CifradoHillMainWindow

class CifradoHillApp(QtWidgets.QApplication):
    def __init__(self, sys_argv):
        super(CifradoHillApp, self).__init__(sys_argv)
        self.main_view = CifradoHillMainWindow()
        self.main_view.show()
