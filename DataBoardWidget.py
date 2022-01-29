from PyQt5.QtWidgets import *

class DataBoardWidget(QTableWidget):
    def __init__(self, parent = None):
        super(DataBoardWidget, self).__init__(parent)
        self.initUi()

    def initUi(self):
        self.setFixedSize(750,450)
        self.setRowCount(10)