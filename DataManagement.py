import BinanceApi

class DataManagement:
    binanceExchangePairs = []
    binanceTicketPrice24h = {}

    def __init__(self):
        BinanceApi.initBinanceApi()
        res = BinanceApi.getBinanceApi().getExchange()
        for item in res:
            self.binanceExchangePairs.append(item["symbol"])