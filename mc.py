import requests
import time
import pandas as pd
from binance.spot import Spot as Client
from CurrentPriceFluctuate import currentPriceFluctuate
import tkinter as tk
import string

exchangeInfo = []

def init():
    BASE_URL = "https://api.binance.com"
    url = BASE_URL + "/api/v3/exchangeInfo"
    res = requests.get(url)
    res = res.json()
    for item in res['symbols']:
        obj = {'symbol': item['symbol'], 'fluctuate_rate': 0}
        exchangeInfo.append(obj)
    currentPriceFluctuate(exchangeInfo, '1d', 0.1)

class ExchangeInfoFrame:
    def __init__(self, window, exchangeInfo = [], rate = 0.05):
        self.frame = None
        self.window = window
        self.exchangeInfo = exchangeInfo
        self.rate = rate

        self.frame = tk.Frame(self.window)
        self.frame.place(relx = "0", rely="0.1", relwidth="1", relheight="0.9")
        self.lb = tk.Listbox(self.frame)
        self.lb.place(relx = "0", rely="0.05", relwidth="0.95", relheight="0.93")
        sb = tk.Scrollbar(self.frame, orient="vertical")
        sb.pack(side="right", fill="y")
        self.lb.configure(yscrollcommand=sb.set)
        sb.config(command=self.lb.yview)
        temList = []
        for item in exchangeInfo:
            tem = item["symbol"] + "     " + str(item["fluctuate_rate"])
            temList.append(tem)

        self.var = tk.StringVar()
        self.var.set(temList)
        self.lb['listvariable'] = self.var
        #self.update(exchangeInfo, rate)

    def isShown(self, item):
        return item['fluctuate_rate'] >= self.rate

    def update(self, exchangeInfo = [], rate = 0.05):
        self.exchangeInfo = exchangeInfo
        self.rate = rate
        fileredExchangeInfo = list(filter(self.isShown, self.exchangeInfo))
        print("filtered:", fileredExchangeInfo)
        self.frame = tk.Frame(self.window);
        self.frame.pack();
        self.exchangeInfo = exchangeInfo
        self.rate = rate
        fileredExchangeInfo = list(filter(self.isShown, self.exchangeInfo))
        print("filtered:", fileredExchangeInfo)
        title1 = tk.Label(self.frame, text="jiaoyidui")
        title1.grid(column = 0, row = 0)
        title2 = tk.Label(self.frame, text="bodong")
        title2.grid(column = 1, row = 0)
        curCount = 0
        for item in fileredExchangeInfo:
            curCount = curCount + 1
            label1 = tk.Label(self.frame, text=item['symbol'])
            label1.grid(column=0, row=curCount)
            label2 = tk.Label(self.frame, text=item['fluctuate_rate'])
            label2.grid(column=1, row=curCount)



def initUI():
    window = tk.Tk()
    window.title("exchange fluctuate")
    window.geometry("800x600")

    #interval select
    intervalChoices = tk.StringVar()
    intervalChoices.set(['1h','1d'])
    intervalChoicesContainer = tk.Listbox(window, listvariable=intervalChoices)
    def listboxSelect(event):
        w = event.widget
        index = (int)(w.curselection()[0])
        val = w.get(index)
        print(val)

    intervalChoicesContainer.bind('<<ListboxSelect>>', listboxSelect)
    intervalChoicesContainer.place( relx = "0.05", rely="0.01", relwidth="0.1", relheight="0.1")

    #rate input
    rateInputContent = tk.StringVar()
    def rateInputCalback(event):
        val = rateInputContent.get().strip()
        if val.isdigit():
            val = int(val)
        else:
            val = 5

        rateInputContent.set(val)
        print("cb:", rateInputContent.get())

    rateInputContainer = tk.Entry(window, textvariable=rateInputContent)
    rateInputContainer.bind('<Leave>', rateInputCalback)
    rateInputContainer.place(relx = "0.3", rely="0.02", relwidth="0.2", relheight="0.08")

    frame = ExchangeInfoFrame(window, exchangeInfo, 0.05)
    window.mainloop()

#init exchangeinfo
init()
print(exchangeInfo)

initUI()