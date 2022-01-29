# from PyQt5.QtGui import *
# from PyQt5.QtCore import *
from PyQt5.QtWidgets import QWidget
class Window(QWidget):
    def __init__(self, parent = None):
        super(Window, self).__init__(parent)
        self.initUi()

    def initUi(self):
        #initialize binance api

        self.setFixedSize(800,600)
