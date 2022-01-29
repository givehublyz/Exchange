import requests


class BinanceApi:
    BASE_URL =  "https://api.binance.com"
    def __init__(self):
        print("init")

    def getPing(self):
        url = BinanceApi.BASE_URL + "/api/v3/ping"
        res = requests.get(url).json()
        return res

    def getServerTime(self):
        url = BinanceApi.BASE_URL + "/api/v3/time"
        res = requests.get(url).json()
        return res
    def getExchange(self):
        url = BinanceApi.BASE_URL + "/api/v3/exchangeInfo"
        res = requests.get(url).json()
        return res

def initBinanceApi():
    global bApi
    bApi = BinanceApi()

def getBinanceApi():
    return bApi