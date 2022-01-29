import requests
import time
import pandas as pd
import tkinter as tk
import string
from binance.spot import Spot as Client
from MainWidget import Window
from PyQt5 import QtWidgets, QtCore
import sys

exchangeInfo = {}
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

