import requests
import time
import pandas as pd
from binance.spot import Spot as Client
import threading

count = 0
class myThread(threading.Thread):
    def __init__(self, urls):
        threading.Thread.__init__(self)
        self.urls=urls

    def run(self):
        for item in self.urls:
            resp = requests.get(item).json()

def currentPriceFluctuate(exchangeList, interval, rate):
    BASE_URL = "https://api.binance.com"
    thread_num = 1
    while thread_num <= 150:
        start = 0
        stride = len(exchangeList) // thread_num
        arr = []
        while start < len(exchangeList):
            i = start
            e = min(start + stride, len(exchangeList))
            ll = []
            while i < e:
                url = BASE_URL + "/api/v3/klines?symbol=" + exchangeList[i]['symbol'] + "&interval=" + interval + "&limit=2"
                ll.append(url)
            arr.append(ll)
            start = start + stride
        start_time = time.time()
        for item in arr:
            t = myThread(item)
            t.start()
            t.join()
        end_time = time.time()
        print("complete time:", end_time - start_time)
        # if len(resp) >= 2 and len(resp[0]) >= 5 and len(resp[1]) >= 5:
        #     pre_price = float(resp[0][4])
        #     after_price = float(resp[1][4])
        #     oneExchangeInfo['fluctuate_rate'] = (after_price - pre_price) / pre_price
        #     #print(oneExchangeInfo['symbol'],":",oneExchangeInfo['fluctuate_rate'])
        # else:
        #     print(oneExchangeInfo['symbol'], " no valid response")
