import requests
import threading
import time
import pandas as pd
from binance.spot import Spot as Client
import tkinter as tk
import string

class UIThread(threading.Thread):
    def __init__(self, exchangeInfo = {}):
        threading.Thread.__init__(self)
        self.exchangeInfo = exchangeInfo

    def listboxSelect(self, event):
        w = event.widget
        index = (int)(w.curselection()[0])
        val = w.get(index)
        print(val)

    def rateInputCalback(self,event):
        val = self.rateInputContent.get().strip()
        if val.isdigit():
            val = int(val)
        else:
            val = 5

        self.rateInputContent.set(val)
        print("cb:", self.rateInputContent.get())

    def mainUI(self):
        window = tk.Tk()
        window.title("exchange fluctuate")
        window.geometry("800x600")

        # interval select
        self.intervalChoices = tk.StringVar()
        self.intervalChoices.set(['1h', '1d'])
        intervalChoicesContainer = tk.Listbox(window, listvariable=self.intervalChoices)

        intervalChoicesContainer.bind('<<ListboxSelect>>', self.listboxSelect)
        intervalChoicesContainer.place(relx="0.05", rely="0.01", relwidth="0.1", relheight="0.1")

        # rate input
        self.rateInputContent = tk.StringVar()
        rateInputContainer = tk.Entry(window, textvariable=self.rateInputContent)
        rateInputContainer.bind('<Leave>', self.rateInputCalback)
        rateInputContainer.place(relx="0.3", rely="0.02", relwidth="0.2", relheight="0.08")

        window.mainloop()

    def run(self):
        print("ui run")
        BASE_URL = "https://api.binance.com"
        self.mainUI()