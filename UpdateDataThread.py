import requests
import threading
import time

class UpdateDataThread(threading.Thread):
    def __init__(self, exchangeInfo = {}):
        threading.Thread.__init__(self)
        self.exchangeInfo = exchangeInfo
        print("data thread init")

    def run(self):
        print("data:")
        BASE_URL = "https://api.binance.com"
        exchangeUrl = BASE_URL + "/api/v3/exchangeInfo"
        with requests.session() as s:
            res = s.get(exchangeUrl).json()
            for item in res['symbols']:
                self.exchangeInfo[item['symbol']] = 0
        print("test:", self.exchangeInfo)

        ticket24hrl = BASE_URL + "/api/v3/ticker/24hr"
        with requests.session() as s:
            res = s.get(ticket24hrl).json()
            for item in res:
                if item['symbol'] == "BTCUSDT":
                    print(item)
        #print("test24h:", res[""])
        # while True:
        #     start = time.time()
        #     print("data update start:")
        #
        #     for key in self.exchangeInfo.keys():
        #         with requests.session() as session:
        #             url = BASE_URL + "/api/v3/klines?symbol=" + key + "&interval=1d&limit=2"
        #             resp = session.get(url).json()
        #             if len(resp) >= 2 and len(resp[0]) >= 5 and len(resp[1]) >= 5:
        #                 pre_price = float(resp[0][4])
        #                 after_price = float(resp[1][4])
        #                 self.exchangeInfo[key] = (after_price - pre_price) / pre_price
        #             else:
        #                 print(key, " no valid response, detail ", resp)
        #     print("data update end", time.time() - start)
        #     time.sleep(60)