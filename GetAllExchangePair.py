import requests

def getAllExchangePair():
    BASE_URL = "https://api.binance.com"
    url = BASE_URL + "/api/v1/exchangeInfo"
    exchangeInfo = {}
    res = requests.get(url).json()
    for item in res['symbols']:
        exchangeInfo[item['symbol']] = 0
    return exchangeInfo